import logging
from pprint import pprint
import re
import sys
from typing import Dict, List

import wikipediaapi

from core.exceptions import CriticalErrors

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(
    logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s')
)
logger.addHandler(handler)


def has_cyrillic(text: str) -> bool:
    """Возвращает True строка содержит буквы кириллического алфавита

    Сложность: O(1)
    """
    return bool(re.search('[а-яёА-ЯЁ]', text))


def if_page_available(article: wikipediaapi.WikipediaPage) -> None:
    """Вызывает ошибку в случае, если статья на Википедии не существует

    Сложность: O(1)
    """
    if article.exists() is False:
        raise CriticalErrors('Cтатья не существует!')
    logger.info('Статья найдена!')


def count_by_letter(dict_animals: Dict[str, List[str]]) -> Dict[str, int]:
    """Подсчитывает число животных в списке,
    хранящихся под ключом(буква русского алфавита)

    В данной задаче число проходов по ключам словаря
    dict_animals будет ограничено числом букв в русском алфавите
    Так что можно считать, что сложность O(1)

    Однако в общем случае O(N), где N - кол-во ключей в словаре dict_animals
    """
    animals_numb: dict = {}
    for letter in dict_animals:
        animals_numb[letter] = len(dict_animals[letter])
        if animals_numb[letter] == 0:
            logger.info(f'Нет зверей на букву {letter}')
    logger.info('Звери посчитаны!')
    return animals_numb


def retrieve_all_animals(
        article: wikipediaapi.WikipediaPage) -> Dict[str, List[str]]:
    """Распределяет животных по ключам от А до Я в зависимости от буквы,
    на которую начинается название животного,
    все названия не на русском в словарь не добавляются

    Сложность: O(N), где N - число животных в статье
    """
    cyrillic_str_lower: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    cyrillic_str_upper: str = cyrillic_str_lower.upper()
    animals: Dict[str, list] = {i: [] for i in cyrillic_str_upper}
    if not isinstance(article, wikipediaapi.WikipediaPage):
        raise CriticalErrors(
            'Неизвестный формат ответа при запросе к эндпоинту!'
        )
    if not isinstance(article.categorymembers, dict):
        raise CriticalErrors(
            'Под ключом categorymembers получен ответ неизвестного формата!'
        )
    logger.info('Получен валидный ответ!')
    for animal in article.categorymembers.values():
        animal_to_append: str = animal.title
        if has_cyrillic(animal_to_append[0]):
            key = animals.get(animal_to_append[0])
            if key is None:
                continue
            else:
                animals[animal_to_append[0]].append(animal_to_append)
        else:
            continue
    return animals


def main() -> None:
    """Основная логика работы программы."""
    logger.info('Начало работы программы!')
    wiki_set: wikipediaapi.Wikipedia = wikipediaapi.Wikipedia('ru')
    page: wikipediaapi.WikipediaPage = wiki_set.page(
        'Категория:Животные по алфавиту'
    )
    try:
        if_page_available(page)
        animals_to_count: Dict[str, List[str]] = retrieve_all_animals(page)
        pprint(count_by_letter(animals_to_count))
        logger.info('Конец работы программы!')
    except CriticalErrors as error:
        logger.error(error)


if __name__ == '__main__':
    main()
