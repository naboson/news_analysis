import json
from news import News

def load(filename):
    with open('./corpus/%s' % filename, 'r', encoding='utf-8') as f:
        data = f.read()
        f.close()
        r = json.loads(data)
        return News(url=r['url'], title=r['title'], content=r['content'])


#d = load('1504367531604b1baa4c81c9c0c31ddf')
# print(data)
# d = json.loads(data)
# print(d['url'])
# print(d['title'])
# print(d['content'])
