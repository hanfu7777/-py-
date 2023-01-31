import settings
from .log_handler import get_logger
# from .config_handler import get_config

# config = get_config('config.yaml')
# 解析这个config.yaml文件
# logger = get_logger(**config['log'])
# 解包这个log的字典
logger = get_logger(**settings.LOG_CONFIG)
# 解包日志配置,给日志收集器
