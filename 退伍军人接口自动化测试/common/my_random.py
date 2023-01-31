import random


def generate_random_str(randomlength, demo='random'):
    """
    :param randomlength: 随机字符串的长度
    :param demo:随机字符串的模式str：只要小写字母，int只要整数
    :return:随机字符串的结果
    """
    random_str = ''

    if demo == 'random':
        base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
    elif demo == 'str':
        base_str = 'abcdefghigklmnopqrstuvwxyz'
    elif demo == 'int':
        base_str = '0123456789'
    else:
        base_str = 666
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


if __name__ == '__main__':
    print(generate_random_str(256, demo='random'))
