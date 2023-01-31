import unittestreport
from datetime import datetime


# 获取当前生成时间前缀

def report(ts, filename=None, report_dir=None, title=None, tester=None, desc=None, templates=None, theme=None):
    """
    执行用例并生成报告
    :param desc:
    :param templates:
    :param ts:
    :param filename:
    :param report_dir:
    :param theme:
    :param title:
    :param desc:
    :param tester:
    :return:
    """
    time_prefix = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    # 拼接到报告文件名
    filename = '{}_{}'.format(time_prefix, filename)
    runner = unittestreport.TestRunner(ts, filename=filename, report_dir=report_dir, title=title, tester=tester,
                                       desc=desc,
                                       templates=templates)
    runner.run()



