import requests
import unittest
import yadisk

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
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

def get_request(text, to_lang):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': to_lang,

    }

    response = requests.get (URL, params = params)
    return response.status_code

class TestGetRequest(unittest.TestCase):

    def test_right_translate(self):
        result = translate_it('Hello', 'ru')
        self.assertEqual('Привет', result)

    def test_good_request(self):
        result = get_request('Hello', 'ru')
        self.assertEqual(200, result)

    def test_wrong_translate(self):
        result = translate_it('Hello', 'ru')
        self.assertNotEqual('пока', result)

    def test_bad_request(self):
        result = get_request('', 'ru')
        self.assertEqual(400, result)

if __name__ == '__main__':
    unittest.main()
