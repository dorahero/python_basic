import json


jsondata = {
    '001': {
        'Name': 'Allen'
    },
    '002': {
        'Name': 'Ted',
        'Interest': ['a', 'b', 'c']
    }
}

json_str = json.dumps(jsondata)      # 將json 物件轉為 string
print(json_str)
print(type(json_str))

with open('test.json', 'w', encoding='utf-8') as f:     # 將此 string 存為 json 檔
    f.write(json_str)

json_data = json.loads(json_str)     # 將json字串轉為 python 中的 json 物件
print(json_data)
print(type(json_data))


