# 1.导包
import requests
# 2.获取地址
url='http://127.0.0.1:8000/api/departments/'
# 3.之际提交数据
my={"$dep_id_list":"T02"}
# 4.发送别接受响应数据
ss=requests.get(url,params=my)
# 5.获取状态码打印
print(ss.status_code)
# 6.获取响应头打印
print(ss.text)