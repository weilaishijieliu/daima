# 1.导包
import pymysql
# 2.创建连接
sw=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',
                   charset='utf8')
# 3.实例化游标
cc=sw.cursor()
try:
    sql1="insert into t_book values(4,'一拳超人','1852-02-9',200,300,0)"
    cc.execute(sql1)
    sql2="insert into t_hero values(6,'光头',1,'必杀技认真的拳',0,4)"
    cc.execute(sql2)
    sw.commit()
except Exception as e:
    print(e)
    sw.rollback()
finally:
    cc.close()
    sw.close()
