# # 1.导包
# import pymysql
# # 2.创建连接
# zj=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',charset='utf8',autocommit=True)
# yb=zj.cursor()
# sql="insert into t_book values(4,'红楼梦','1990-08-3',300,200,0)"
# yb.execute(sql)
# zj.close()
# yb.close()`
# import pymysql
# conn=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',charset='utf8',autocommit=True)
# cursor=conn.cursor()
# sql='delete from t_book where id=4'
# cursor.execute(sql)
# cursor.close()
# conn.close()
# import pymysql
# cc=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',charset='utf8',autocommit=True)
# aa=cc.cursor()
# sql='update t_book set title="水浒" where id=3'
# aa.execute(sql)
# cc.close()
# aa.close()