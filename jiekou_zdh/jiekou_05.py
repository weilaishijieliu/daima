
# from jiekou_zdh.laoshi1 import MyDBUtil
from jiekou_zdh.gongju_04 import GongJu
import jiekou_zdh.gongju_04
c=GongJu.getConn()
cc=GongJu.youBao(c)
# print(c)
# print(cc)
sql='select * from t_book'
cc.execute(sql)
cc.
rows = cc.fetchall()
# print(rows)
for a in rows:
    print(a)
GongJu.shiFhang(c,cc)