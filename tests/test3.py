import unittest

from tasks.task3 import (if_even, split_into_pairs,
                         interval_by_second, appearance)
from core.dummy_data import tests


class TestTaskThree(unittest.TestCase):
    """Тестируем третье задание."""

    @classmethod
    def setUp(cls):
        cls.even_odd = {8: True, 0: True, 5: False}
        cls.unpaired_paired = (
            ([1, 2, 3, 4], [[1, 2], [3, 4]]), ([5, 6], [[5, 6]])
        )
        cls.interval = [[1, 10], [20, 30]]
        cls.lesson = [[15, 25]]

    def test_if_even(self):
        """Тестируем if_even"""
        for num, result in TestTaskThree.even_odd.items():
            with self.subTest(num=num):
                self.assertEqual(
                    if_even(num), result,
                    f'Функция if_even возвращает {num} для {result}')

    def test_split_into_pairs(self):
        """Тестируем split_into_pairs"""
        for unpaired, paired in TestTaskThree.unpaired_paired:
            with self.subTest(unpaired=unpaired):
                self.assertEqual(
                    split_into_pairs(unpaired), paired,
                    f'Получили {split_into_pairs(unpaired)} вместо {paired}'
                )

    def test_interval_by_second(self):
        """Тестируем split_into_pairs"""
        result = interval_by_second(
            TestTaskThree.interval, TestTaskThree.lesson
        )
        expected = {20, 21, 22, 23, 24}
        self.assertEqual(
            result, expected,
            f'Получили {result} вместо {expected}'
        )

    def test_appearance(self):
        """Тестируем appearance"""
        for i, test in enumerate(tests):
            with self.subTest(i=i):
                data_to_parse = test['data']
                test_answer = appearance(data_to_parse)
                self.assertEqual(
                    test_answer, test['answer'],
                    f'Error on test case {i},'
                    f'got {test_answer}, expected {test["answer"]}')
