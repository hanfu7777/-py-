import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 日志配置
LOG_CONFIG = {
    'name': os.path.join(BASE_DIR, '退伍军人'),
    'filename': os.path.join(BASE_DIR, 'logs/退伍军人自动化日志.log'),
    'debug': True
}

# 测试数据配置
TSET_DATA_FILE = {
    'file': os.path.join(BASE_DIR, 'TestData/TestCases.xlsx'),
    'sheet1': '退伍军人_数据分发'
}
# 鉴权    注意换环境更改TestCases.xlsx用例中的url和TOKEN信息
# 主要的账号   这里一般使用账号  hanfu/hanfu123456
TOKEN = {
    'username': 'dagly',
    'password': 'dagly123456',
    'url': 'http://192.168.0.253:8080/gateways/login'
}

if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_CONFIG.get('name'))
    print(LOG_CONFIG.get('filename'))
    print(TSET_DATA_FILE.get('file'))
