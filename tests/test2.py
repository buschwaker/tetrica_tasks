import unittest
import wikipediaapi

from tasks.task2 import has_cyrillic, if_page_available, count_by_letter


class TestTaskTwo(unittest.TestCase):
    """Тестируем второе задание."""

    @classmethod
    def setUp(cls):
        cls.russian_english = {'Алфавит': True, 'Alphabet': False}
        wiki_set = wikipediaapi.Wikipedia('ru')
        cls.page = wiki_set.page(
            'Пушкин'
        )
        cls.non_existed = wiki_set.page(
            'Какая-то несуществующая статья'
        )
        cls.letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
        cls.dict_to_count = {
            letter: [i for i in range(j)]
            for j, letter in enumerate(cls.letters)
        }

    def test_has_cyrillic(self):
        """Тестируем функцию test_has_cyrillic"""
        for word, result in TestTaskTwo.russian_english.items():
            with self.subTest(word=word):
                self.assertEqual(
                    has_cyrillic(word), result,
                    f'Функция has_cyrillic должна вернуть {result} для {word}'
                )

    def test_if_available_page(self):
        """тестируем что вызов существующей статьи не вызывает ошибок"""
        self.assertIsNone(
            if_page_available(TestTaskTwo.page),
            'Вызов if_available_page для '
            'существующей страницы не должен вызвать ошибок'
                          )

    @unittest.expectedFailure
    def test_if_unavailable_page(self):
        """тестируем что вызов несуществующей статьи вызывает ошибку"""
        self.assertIsNone(
            if_page_available(TestTaskTwo.non_existed),
            'Вызов if_available_page для '
            'несуществующей страницы должен вызвать ошибку')

    def test_count_by_letter(self):
        """Тестируем что при вызове test_count_by_letter со словарем длина
        значений которого известна,
        функция подсчитывает эти длины корректно
        """
        results = count_by_letter(TestTaskTwo.dict_to_count)
        i = 0
        for letter, length in results.items():
            with self.subTest(letter=letter):
                self.assertEqual(
                    length, i,
                    f'Для ключа{letter} кол-во элементов в'
                    f' value должно было быть {i}, {length} вместо этого'
                )
                i += 1
