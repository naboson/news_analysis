import parse
import save


url_list = [
    'https://udn.com/news/story/6813/2515948',
    'https://udn.com/news/story/6813/2515978',
    'https://udn.com/news/story/6813/2515977',
    'https://udn.com/news/story/6813/2515931',
    'https://udn.com/news/story/6813/2515838',
    'https://udn.com/news/story/6813/2515735'
]

for url in url_list:
    news = parse.parse_news(url=url)
    save.save(news=news)
    print('saved...%s' % url)
