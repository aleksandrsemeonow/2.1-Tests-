from datetime import datetime
import yadisk
import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
path_all = [ 'DE.txt', 'ES.txt', 'FR.txt' ]
token = 'AgAAAAAH_QAQAAXkX7xLlzVVVE9HhDkQ57m_j1k'
y = yadisk.YaDisk (token = token)

def translate_it(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': to_lang,

    }

    response = requests.get (URL, params = params)
    json_ = response.json ()
    return ''.join (json_[ 'text' ])


def write_to_file():
    y.mkdir('/Translate')
    for path in path_all:
        with open(path) as f:
            lang_list = []
            for line in f:
                line = line.strip()
                lang_list.append(line)

        with open(f'translatefrom_{path[:2]}.txt', 'w', encoding='UTF-8') as new:
            new.write((translate_it(lang_list, 'ru')))
        with open(f'translatefrom_{path[:2]}.txt', 'rb') as f:
            y.upload(f, f'Translate/translatefrom_{path[:2]}.txt')


