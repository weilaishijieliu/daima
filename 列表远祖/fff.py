from

with open("../Data/search_page.yaml", 'r') as f:
    data = yaml.load(f)
    print(type(data))  # 打印data类型
    print(data)  # 打印data返回值