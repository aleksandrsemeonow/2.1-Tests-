from Task_2 import translate
import unittest


class TestGetRequest(unittest.TestCase):

    def right_translate(self):
        self.assertEqual('привет', translate.translate_it('Hello', 'ru'))

if __name__ == '__main__':
    unittest.main()