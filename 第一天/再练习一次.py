# 导包
import logging.handlers
# 实例化，获取日志



class Logger:
    logger=None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.longger=logging.getLogger()
            # 设置日志级别，实例化名称，设置等级（记录，等级）
            cls.longger.setLevel(logging.INFO)
            # 获取处理器控制台，变量名=记录处理器
            sh=logging.StreamHandler()
            # 设置处理器(保存文件位置
            tr=logging.handlers.TimedRotatingFileHandler(filename='./aawa.log',when='midnight',interval=1,backupCount=30,encoding='utf-8')
            # 定义文件格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"

            # 变量名，文件处理器（文件格式）
            fm=logging.Formatter(fmt)
            # 控制台，格式器（文件处理器）\
            sh.setFormatter(fm)

            # 处理器，格式器（文件处理器）
            tr.setFormatter(fm)
            # 实例化，增加（控制器）
            cls.logger.addHandler(sh)
            # 实例化，增加（处理器）
            cls.longger.addHandler(tr)
        return cls.logger
Logger().get_logger()

