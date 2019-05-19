import requests
my=  {
                "data": [
                        {
                            "dep_id":"T02",
                            "dep_name":"嘻哈学院",
                            "master_name":"Test-Master",
                            "slogan":"Here is Slogan"
                        }
                  ]
            }
url='http://127.0.0.1:8000/api/departments/T02/'
re=requests.put(url,json=my)
print(re.status_code)
print(re.text)