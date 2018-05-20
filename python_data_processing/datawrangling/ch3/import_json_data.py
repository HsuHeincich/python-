import json

json_data = open('E:/xhy_python/data-wrangling-master/data/chp3/data-text.json').read()

data = json.loads(json_data)

for item in data:
    print item