import requests
import json


def login(username, password, url):
    """
    :param username: 用户名
    :param password: 密码
    :param url: 获取token的url地址
    :return: 响应消息，具体token的值需要调试一下
    """
    res = requests.post(url=url, json=
    {
        "password": password,
        "username": username
    },
                        headers={'Content-Type': 'application/json'}).text
    res = json.loads(res)
    # 反序列化  json -> dict
    return res


if __name__ == '__main__':
    token = login("dagly", "dagly123456", "http://192.168.0.253:8080/gateways/login")['data']
    # 获取响应消息中data中的token
    print(token, type(token))
