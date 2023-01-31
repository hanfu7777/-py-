import logging


def get_logger(name, filename, mode='a', encoding='utf-8', fmt=None, debug=True):
    """
    :param name: 日志器的名子
    :param filename: 日志文件名
    :param fmt: 日志格式
    :param debug: 调试模式
    :param mode:文件模式
    :param encoding：字符编码
    :return:
    """
    # 创建日志器  这个系统一般会有多个日志器，以名称去区分，没有实际意义
    logger = logging.getLogger(name)
    # 日志器可以设置等级   创建日志的时候生效
    logger.setLevel(logging.DEBUG)
    # 判断是否为调试模式(是的话工作台和日志都输入debug的内容，不是的话工作台和日志都输出info级别以上的内容)
    # DEBUG的级别是最低的
    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.DEBUG
    if fmt is None:
        fmt = '%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s'
    # 创建文件日志处理器 日志处理器也可以设置等级
    file_handler = logging.FileHandler(filename=filename, mode=mode, encoding=encoding)
    file_handler.setLevel(file_level)
    # 创建工作台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    # 创建格式化器
    formatter = logging.Formatter(fmt=fmt)
    # 将格式化器添加到日志器上
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 将日志处理器添加到日志器上
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger('han', '../logs/han_test.log', debug=True)
    logger.error("I am general information")
    logger.info("I am info")
    logger.debug("I am debug")
    logger.warning("I am warning")
    logger.critical("I am critical ")
