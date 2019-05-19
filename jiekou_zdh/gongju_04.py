import pymysql
class GongJu:
    # 封装连接
    @classmethod
    def getConn(cls):
        conn = pymysql.Connect(host='127.0.0.1', port=3306, database='books', user='root', password='root',
                              charset='utf8', autocommit=True)
        return conn

    # 封装游标
    @classmethod
    def youBao(cls,c):

        return c.cursor()

    # 封装释放内存
    @classmethod
    def shiFhang(cls, c, conn):
        if c:
            c.close()
            # cursor = None
        if conn:
            conn.close()
            # conn = None