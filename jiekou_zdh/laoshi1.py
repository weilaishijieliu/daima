# 新建 pymysql 使用的工具类
import pymysql
class MyDBUtil:
    # 封装获取连接、游标，以及释放资源的函数
    #1、封装获取连接的实现
    @classmethod
    def getConn(cls):
        conn = pymysql.connect(host="127.0.0.1", port=3306, database="books",
                               user="root", password="root",charset="utf8")
        return conn
    #2、封装获取游标的实现
    @classmethod
    def getCursor(cls, conn):
        return conn.cursor()

    #3、编写释放资源的实现
    @classmethod
    def closeResource(cls, cursor, conn):
        if cursor :
            cursor.close()
            cursor = None
        if conn :
            conn.close()
            conn = None