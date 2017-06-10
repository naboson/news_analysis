from bs4 import BeautifulSoup
import requests
from news import News


def parse_news(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # 1. get title
    title = soup.find(id='story_art_title').string

    # 2. get content
    content = ''

    body = soup.find(id='story_body_content')
    for i in body.contents:
        if i.name == 'p' and i.string is not None:
            content += i.string

    return News(url=url, title=title, content=content)
