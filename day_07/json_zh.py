import json

# date={"名字“："小明"，"年龄"：18}
da = {"名字":"小明","age":20}
with open('../case/www.json,','w',encoding='utf-8') as f:
    json.dump(da,f,ensure_ascii=False)

with open('../case/www.json','r') as f:
    json.load(www.json)