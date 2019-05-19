import yaml

def analyze_data(filename, keycase):
    filepath = "./data/" + filename
    with open(filepath, 'r', encoding='utf-8')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[keycase]
        data_list = list()
        data_list.extend(data.values())
        return data_list

