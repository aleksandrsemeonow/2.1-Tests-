import unittest
from Task_1 import function
from Task_1.directories import directories
from Task_1.documents import documents


class TestGetDocuments(unittest.TestCase):

    def setUp(self) -> None:
        self.directories = directories
        self.documents = documents

    def test_add_doc_on_directories(self):
        len_doc = len(self.directories['2'])
        function.add_docs('505050', 'snils', '2')
        self.assertGreater(len(self.directories['2']), len_doc)

    def test_find_docs(self):
        self.assertEqual('Василий Гупкин', function.people('2207 876234'))

    def test_delete_doc_from_directories(self):
        len_doc = len(self.directories['1'])
        function.delete_doc('2207 876234')
        self.assertLess(len(self.directories['1']), len_doc)

if __name__ == '__main__':
    unittest.main()