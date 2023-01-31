import pytest


@pytest.fixture(scope='class')
def class_fixture():
    print(f'\n{"*" * 30}测试用例类开始执行{"*" * 30}')
    yield
    print(f'\n{"*" * 30}测试用例类执行结束{"*" * 30}')
