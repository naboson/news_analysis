import json


def load(filename):
    with open('./corpus/%s' % filename, 'r', encoding='utf-8') as f:
        data = f.read()
        f.close()
        return json.loads(data)


d = load('1504367531604b1baa4c81c9c0c31ddf')
# print(data)
# d = json.loads(data)
print(d['url'])
print(d['title'])
print(d['content'])
