import uuid
import json


def save(news):
    data = {
        'url': news.get_url(),
        'title': news.get_title(),
        'content': news.get_content()
    }

    id = str(uuid.uuid4()).replace('-', '')
    with open('./test/%s' % id, 'a+') as f:
        f.write(json.dumps(data, ensure_ascii=False))
        f.close()
