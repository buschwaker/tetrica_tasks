import logging
import sys

from core.exceptions import CriticalErrors
from core.dummy_data import tests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(
    logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s')
)
logger.addHandler(handler)


def if_even(a):
    """Возвращает True, если число четное"""
    return a % 2 == 0


def split_into_pairs(a):
    """Разделяет последовательность на пары,
    упаковывая их в двухмерный массив"""
    if not if_even(len(a)):
        raise CriticalErrors('Число входов и выходов пользователя различно!')
    if not isinstance(a, list):
        raise CriticalErrors('Неизвестный формат данных о посещении урока!')
    q = 0
    some_list = []
    for j in range(int(len(a) / 2)):
        some_list.append([a[q+j], a[q+j+1]])
        q += 1
    return some_list


def interval_by_second(a, limit):
    seconds_online = set()
    for q in range(len(a)):
        for sec in range(a[q][0] if a[q][0] > limit[0][0] else limit[0][0],
                         a[q][1] if a[q][1] < limit[0][1] else limit[0][1]):
            seconds_online.add(sec)
    return seconds_online


def count_seconds_together(a, b):
    interval_together = a.intersection(b)
    return len(interval_together)


def appearance(data):
    """Основная логика работы программы."""
    logger.info('Начало работы программы!')
    try:
        pair_lesson = split_into_pairs(data['lesson'])
        pair_pupil = split_into_pairs(data['pupil'])
        pair_tutor = split_into_pairs(data['tutor'])
        tutor_time = interval_by_second(pair_tutor, pair_lesson)
        pupil_time = interval_by_second(pair_pupil, pair_lesson)
        return count_seconds_together(tutor_time, pupil_time)
    except CriticalErrors as error:
        logger.error(error)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], (
            f'Error on test case {i},'
            f'got {test_answer}, expected {test["answer"]}'
        )
        logger.debug('Tecт пройден!')
