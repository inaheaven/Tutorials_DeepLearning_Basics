import codecs
import json

def load_jsonfile(fname):
    try:
        with codecs.open(fname, 'rb', encoding='utf-8') as f:
            lines = f.read()
            json_data = json.loads(lines)
            return json_data
    except Exception as e:
        print("error:", e)

mydata = load_jsonfile("exercise2.json")
print(mydata)


d1 = mydata['member']['name']
print(d1)
d2 = mydata['member']['address']
print(d2)
d3 = mydata['member']['phone']
print(d3)
d4 = mydata['web']['cafe']
print(d4)
d5 = mydata['web']['id']
print(d5)