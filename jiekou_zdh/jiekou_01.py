# python链接数据库基本框架
# 1.整合第三方pymysql
import pymysql
# 2.创建连接
# 调用Connect函数
cj=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',charset='utf8')
# 3.创建游标
# cursor=cj.cursor(7)
cursor=cj.cursor()
# 4.发送SQL语句
sql='select * from t_book'
# 执行语句
cursor.execute(sql)
# 获取查询行数
# hs=cursor.rowcount
# print('行数',hs)
# 获取结果
jg=cursor.fetchall()
print('结果',jg)
# for a in jg:
#     print(a)
#     print('编号:',a[0])
#     print('书名:',a[1])
#     print('时间:',a[2])
#     print('阅读数:',a[3])
#     print('评论数:',a[4])
#     print('是否删除:',a[5])
#     print('---------------------')
# print(cursor.fetchone())

# 5.资源释放
cursor.close()
cj.close()