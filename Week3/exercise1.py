import json

data = {
    'age': 30,
    'name': '홍길동',
    'address' : 'mapo',
    'broadcast': {
        'sbs':5,
        'mbc':11
    }
}

json_data = json.dumps(obj=data, indent=4)
print(json_data)
print(type(json_data))

json_data2= json.loads(json_data, encoding='utf-8')
print(json_data2)
print(type(json_data2))

json_data = json.dumps(data, sort_keys=False, indent=4)
print(json_data)
print(type(json_data))