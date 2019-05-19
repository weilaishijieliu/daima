import requests
# 获取session对象
s=requests.session()
# 使用session对象发验证码
rr=s.get('http://localhost:8088/index.php?m=Home&c=User&a=verify ')
print(rr.status_code)
print(rr.content)
print("-"*80)
# 使用session对象发送登录请求
myData = {
    "username":"13012345678",
    "password":"123456",
    "verify_code":"8888"
}
rr = s.post("http://localhost:8088/index.php?m=Home&c=User&a=do_login",data=myData)
print(rr.status_code)
print(rr.json())
