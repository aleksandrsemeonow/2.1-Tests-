import unittest
from unittest.mock import patch
from Task_1 import main
from Task_1.directories import directories
from Task_1.documents import documents

class TestGetDocuments(unittest.TestCase):

    def setUp(self) -> None:
        self.directories = directories.copy()
        self.documents = documents.copy()

    def test_find_docs(self):
        self.assertEqual('Геннадий Покемонов', main.people('11-2'))

    def test_add_doc_on_directories(self):
        len_doc = len(self.directories['2'])
        main.add_docs('505050', 'snils', '2')
        self.assertGreater(len(self.directories['2']), len_doc)

    def test_delete_doc_from_directories(self):
        len_doc = len(self.directories['1'])
        with patch('Task_1.documents', self.documents),\
            patch('Task_1.directories', self.directories):
            main.delete_doc('2207 876234')
        self.assertLess(len(self.directories['1']), len_doc)

if __name__ == '__main__':
    unittest.main()
