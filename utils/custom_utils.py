from typing import List

import requests

from bs4 import BeautifulSoup

import re


def get_categories_with_hashtags(categories: str) -> str:
    categories_with_hashtags = ''
    for category in categories:
        categories_with_hashtags += f'#{category} '
    return categories_with_hashtags


def parsing(url: str) -> List[str, str]:
    base_url = url[:url.find('.site') + 5]

    response = requests.get(url)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    img = soup.find('div', {'class': 'img'}).find('img').get('src')
    title = soup.find('div', {'class': 'film'}).find('h1').text
    hd = soup.find('span', {'class': 'icon-hd'}).text
    category = soup.find('div', {'class': 'category'}).text
    category = category.replace('Фильмы', '').replace('Категории', '')

    numbers = re.findall(r'[\d]+', category)

    if numbers:
        for number in numbers:
            category = category.replace(number, '')
        category = category.split()
    else:
        category = category.split()
    try:
        imdb_count = soup.find('div', {'class': 'imdb-count'}).text
        imdb_count = '.'.join(re.findall(r'[\d]+', imdb_count))
    except AttributeError:
        imdb_count = None

    description = soup.find('div', {'class': 'description'}).find_all('span')[-1].text.replace('\n', '').replace(
        '\t', '').replace('\xa0', ' ')

    description_replace = description[:description.find('совершенно бесплатно') + len('совершенно бесплатно')]
    description = description.replace(description_replace, '')

    data = {
        'title': title,
        'hd': hd,
        'category': category,
        'imdb_count': imdb_count,
        'description': description
    }
    text = (
            f'''**🎬 [{data['title']} {data['hd']}]({base_url+img})**
            **🍿Жанр:** {get_categories_with_hashtags(data['category'])}''' +
            ('''**⭐Рейтинг КиноПоиск:**''' + data['imdb_count']) if data['imdb_count'] else '' +
            f'''

            🔊{data['description']}
            
            [🎬 Смотреть онлайн]({url})
            [👉 Все фильмы](http://f1.ikino.site/filmy/) | [👉 Все сериалы](http://f1.ikino.site/serialy/)'''
    )
    return [text, url]
