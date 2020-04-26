import requests
from bs4 import BeautifulSoup
import re


def categories(cat):
    result = ''
    for i in cat:
        result += f'#{i} '
    return result


def parsing(url):
    page = requests.get(
        url
    )
    page.encoding = 'utf-8'
    base_url = url[:url.find('.site')+5]
    soup = BeautifulSoup(page.text, 'html.parser')

    img = soup.find(
        'div', {
            'class': 'img'
        }
    ).find(
        'img'
    ).get('src')

    title = soup.find('div', {
        'class': 'film'
    }).find('h1').text

    hd =soup.find('span', {
        'class': 'icon-hd'
    }).text

    category = soup.find(
        'div', {
            'class': 'category'
        }
    ).text
    category = category.replace('Фильмы', '').replace('Категории', '')

    numbers = re.findall(r'[\d]+', category)

    if numbers:
        for i in numbers:
            category = category.replace(i, '')
        category = category.split()
    else:
        category = category.split()
    try:
        imdb_count = soup.find(
            'div', {
                'class': 'imdb-count'
            }
        ).text
        imdb_count = '.'.join(re.findall(r'[\d]+', imdb_count))
    except:
        imdb_count = None

    description = soup.find(
        'div', {
            'class': 'description'
        }
    ).find_all(
        'span'
    )[-1].text.replace(
        '\n', ''
    ).replace(
        '\t', ''
    ).replace(
        '\xa0', ' '
    )

    description = description.replace(description[:description.find('совершенно бесплатно')+21], '')

    data = [title, hd, category, imdb_count, description]
    if data[3]:
        text = f'''**🎬 [{data[0]} {data[1]}]({base_url+img})**
**🍿Жанр:** {categories(data[2])}
**⭐Рейтинг КиноПоиск:** {data[3]}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://f1.ikino.site/filmy/) | [👉 Все сериалы](http://f1.ikino.site/serialy/)'''
    else:
        text = f'''**🎬 [{data[0]} {data[1]}]({base_url+img})**
**🍿Жанр:** {categories(data[2])}

🔊{data[4]}

[🎬 Смотреть онлайн]({url})
[👉 Все фильмы](http://f1.ikino.site/filmy/) | [👉 Все сериалы](http://f1.ikino.site/serialy/)'''
    return text, url