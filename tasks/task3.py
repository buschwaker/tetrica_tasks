import logging
import sys
from typing import Dict, List, Set, Optional, Union

from core.exceptions import CriticalErrors
from core.dummy_data import tests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(
    logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s')
)
logger.addHandler(handler)


def if_even(a: int) -> bool:
    """Возвращает True, если число четное"""
    return a % 2 == 0


def split_into_pairs(a: List[int]) -> List[List[int]]:
    """Разделяет последовательность на пары,
    упаковывая их в двухмерный массив"""
    if not if_even(len(a)):
        raise CriticalErrors('Число входов и выходов пользователя различно!')
    if not isinstance(a, list):
        raise CriticalErrors('Неизвестный формат данных о посещении урока!')
    q: int = 0
    some_list: list = []
    for j in range(int(len(a) / 2)):
        some_list.append([a[q+j], a[q+j+1]])
        q += 1
    return some_list


def interval_by_second(a: List[List[int]],
                       limit: List[List[int]]) -> Set[int]:
    """Создает множество состоящее из секунд проведенных
    пользователем в сервисе, учитывает также продолжительность
    урока, отсекая время проведенное вне его
    """
    seconds_online: set = set()
    for q in range(len(a)):
        for sec in range(a[q][0] if a[q][0] > limit[0][0] else limit[0][0],
                         a[q][1] if a[q][1] < limit[0][1] else limit[0][1]):
            seconds_online.add(sec)
    return seconds_online


def count_seconds_together(a: Set[int], b: Set[int]) -> int:
    """Возвращает время в секундах которое ученик
    и учитель провели на уроке вместе
    """
    interval_together = a.intersection(b)
    return len(interval_together)


def appearance(data: Union[int, Dict[str, List[int]]]) -> Optional[int]:
    """Основная логика работы программы."""
    logger.info('Начало работы программы!')
    if isinstance(data, int):
        raise CriticalErrors('Для переменной data ожидался словарь!')
    try:
        pair_lesson: List[List[int]] = split_into_pairs(data['lesson'])
        pair_pupil: List[List[int]] = split_into_pairs(data['pupil'])
        pair_tutor: List[List[int]] = split_into_pairs(data['tutor'])
        tutor_time: Set[int] = interval_by_second(pair_tutor, pair_lesson)
        pupil_time: Set[int] = interval_by_second(pair_pupil, pair_lesson)
        return count_seconds_together(tutor_time, pupil_time)
    except CriticalErrors as error:
        logger.error(error)
    return None


if __name__ == '__main__':
    for i, test in enumerate(tests):
        data_to_parse: Union[int, Dict[str, List[int]]] = test['data']
        test_answer: Optional[int] = appearance(data_to_parse)
        assert test_answer == test['answer'], (
            f'Error on test case {i},'
            f'got {test_answer}, expected {test["answer"]}'
        )
        logger.debug('Tecт пройден!')
