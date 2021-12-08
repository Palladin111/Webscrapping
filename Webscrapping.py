import requests
from bs4 import BeautifulSoup
import re

MY_HUBS = ['дизайн', 'фото', 'web', 'python']

response = requests.get("https://habr.com/ru/all/", timeout=15, headers={"User-Agent":"Mozilla/5.0 "})
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article')

title_1 = []
for article in articles:
    for hub in MY_HUBS:
        pattern_hub = re.compile("({})".format(hub))
        result = pattern_hub.findall(article.text)
        if hub in result:
            date = article.find('time').attrs.get('title')
            title = article.find('h2')
            link = title.find('a').attrs.get('href')
            url = "https://habr.com" + link
            if title.text not in title_1:
                print(f'{date[0:10]} - {title.text} - {url}')
                title_1.append(title.text)
