import json
import re
import settings
import time
from common.make_requests import send_http_requests
from common.Test_data_handler import get_test_data_from_excel, replace_args_by_re
from common import logger, get_token
from common.my_random import generate_random_str
import pytest

# 直接导入了__init__中实例好的模块

cases = get_test_data_from_excel(settings.TSET_DATA_FILE['file'], settings.TSET_DATA_FILE['sheet1'])


# 直接导入配置文件的库，就可以直接用配置文件的大字典了。配置文件已经封装好了大字典，所以可以直接参数化

@pytest.mark.parametrize('case', cases)
class Test_config:
    logger = logger
    # 获取一个随机的类型长度为5的名称
    proper_name = str(generate_random_str(5, 'random'))

    @pytest.mark.usefixtures('class_fixture')
    def test(self, case):
        # 获取全新的token------具体项目具体分析
        if "#token#" in case.get("headers"):
            token = get_token.login(**settings.TOKEN)['data']
            # 替换槽位
            case['headers'] = case['headers'].replace("#token#", token)
        # 如果json中有##包裹的字段,就要进行替换
        if re.findall('#.*?#', case.get('json')):
            # 获取一个超长的名称
            self.__class__.super_long = str(generate_random_str(256, 'random'))
            case['json'] = replace_args_by_re(case['json'], self)
        self.logger.info(f"用例【{case['title']}】开始测试,这是第【{case['case_id']}】条用例\n发起请求的地址是------>:{case['url']}")
        #  进行反序列化
        case['json'] = json.loads(case['json'])
        case['expected'] = json.loads(case['expected'])
        case['headers'] = json.loads(case['headers'])
        case['files'] = json.loads(case['files'])
        # 如果需要上传文件的话
        if case['files'].get('path', 0):
            files = {
                "file": (case['files']['filename'], open(case['files']['path'], "rb"), 'application/json')
            }
            response = send_http_requests(url=case['url'], method=case["method"], headers=case['headers'],
                                          data=case['json'], files=files)
            response_data = response.json()
        # 否则默认这样上传
        else:
            response = send_http_requests(url=case['url'], method=case["method"], headers=case['headers'],
                                          json=case['json'])
            # 以json的形式展现
            response_data = response.json()
        # 断言
        try:
            # 状态码断言
            assert case['expected']['code'] == int(response_data['code'])
            print(f"测试【{case['title']}】响应状态码断言成功")
            # 响应数据断言
            assert case['expected']['message'] == response_data['message']
            print(f"测试【{case['title']}】数据内容断言成功")
        except AssertionError as e:
            # 写入错误日志
            self.logger.warning(f"断言失败----期望结果是>>>>>>>:{case['expected']}-----响应结果是>>>>>>>:{response_data}")
            # 打印错误内容
            print(f"断言失败----期望结果是>>>>>>>:{case['expected']}-----响应结果是>>>>>>>:{response_data}")
            raise e
        else:
            self.logger.info(f"用例【{case['title']}】测试通过-----------响应消息为{response_data}")
        finally:
            self.logger.info(f"<<<<<<<<<<<<<<<<<用例【{case['title']}】测试结束>>>>>>>>>>>>>>>>>")
