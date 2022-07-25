from typing import Union, Optional, List


def task(array: Union[str, List[float], List[str]], level: int = None,
         first_group_num: Union[float, str] = None) -> Optional[int]:
    """Функция, принимает последовательность
    состоящей из двух групп единиц и нулей(в общем случае любых знаков)
    возвращает индекс последнего элемента группы

    Сложность: O(N), где N - длина последовательности array

    >>> dummy_data = "111111111110000000000000000"
    >>> task(dummy_data)
    11
    >>> task(dummy_data[::-1])
    16
    >>> task('')
    Пустой массив
    >>> task([i for i in dummy_data]) # список строк
    11
    >>> task([int(i) for i in dummy_data]) # список целых чисел
    11
    >>> task("1111111111")
    Всего одна группа знаков!

    """
    if len(array) == 1:
        print('Всего одна группа знаков!')
        return None
    if len(array) == 0:
        print('Пустой массив')
        return None
    first_group_num = first_group_num or array[0]
    level = level or 0
    if first_group_num != array[0]:
        return level
    return task(array[1:], level=level + 1, first_group_num=first_group_num)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
