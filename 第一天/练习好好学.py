# 导包，记录操作
import logging.handlers
# 获取日志器
# 实例化=记录，记录器
logger=logging.getLogger()
# 设置日志级别
# 实例化名称。设置等级(记录，等级)
logger.setLevel(logging.INFO)
# 获取处理器控制台
# 变量名=记录，处理器
sh=logging.StreamHandler()
# 处理器
# 变量名=记录操作者定时
tf=logging.handlers.TimedRotatingFileHandler(filename='./aaa.log',when='midnight',interval=1,backupCount=30,encoding='utf-8')
# 文件格式
# 设置文件格式
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
# 变量名=记录，文件处理器（fmt）
fm=logging.Formatter(fmt)
# 将格式器添加到处理器控制台
# 控制台，格式器（文件处理器）
sh.setFormatter(fm)
# 将格式器添加到 处理器 文件 m
# 处理器，格式器（文件处理器）
tf.setFormatter(fm)
# 将处理器添加到 日志器
# 实例化，增加（控制器）
logger.addFilter(sh)
# 实例化，增加（处理器）
logger.addFilter(tf)