import unittest


from tasks.task1 import task


class TestTaskOne(unittest.TestCase):
    """Тестируем первое задание"""

    @classmethod
    def setUp(cls):
        cls.str_one_zero = "111111111110000000000000000"
        cls.str_one = '11111111'
        cls.data = (
            (cls.str_one_zero, 11),
            (cls.str_one_zero[::-1], 16),
            ([i for i in cls.str_one_zero], 11),
            ([int(i) for i in cls.str_one_zero], 11),
            (cls.str_one, None)
        )

    def test_str(self):
        """Тестируем результаты вызова функции task с различными аргументами"""
        for sequence_result in TestTaskOne.data:
            with self.subTest(sequence=sequence_result):
                self.assertEqual(
                    task(sequence_result[0]), sequence_result[1],
                    f'Вызов функции task с {sequence_result[0]}'
                    f' должен был вернуть {sequence_result[1]}'
                )


if __name__ == '__main__':
    unittest.main()
