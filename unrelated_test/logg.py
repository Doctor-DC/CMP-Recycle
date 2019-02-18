import logging

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger('djang')


# def index(request):
logger.warning("这是一个错误信息1....")
logger.info("这是一个信息")
logger.info("这是一个调试信息2....")

    # collect_logger.info("用户：北京")