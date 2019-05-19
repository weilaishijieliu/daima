# 第一步：定义一个函数继承filename
def read_txt(filename):
    # 变量名=文件路径+filename

    filepath = "../data/"+filename


    # 用打开（文件名变量‘读取’国际编码）as f
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt("login.txt"))
    print(" - -" * 50)
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))

    print(arrs[1:])
    filepath = "../data/"+filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt("login.txt"))
    print(" - -" * 50)
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))

    print(arrs[1:])