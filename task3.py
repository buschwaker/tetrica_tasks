pupil = [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472]
tutor = [1594663290, 1594663430, 1594663443, 1594666473]
# tutor_in_out = [[second, 'in' if i % 2 == 0 else 'out'] for i, second in enumerate(tutor)]
# student_in_out = [[second, 'in' if i % 2 == 0 else 'out'] for i, second in enumerate(pupil)]
lesson = [1594663200, 1594666800]

pupil_in_out_by_sec = []
# tutor = [[1594663290, 1594663430, ], [1594663443, 1594666473]]
# pupil = [[1594663340, 1594663389,], [1594663390, 1594663395] , [1594663396, 1594666472]]


def check_sorted(a, ascending=True):
    """Возвращает True, если последовательность отсортирована.
    С помощью параметра ascending можно задать направление сортировки
    """
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(a) - 1):
        if s*a[i] > s*a[i+1]:
            flag = False
            break
    return flag


def if_even(a):
    """Возвращает True, если число четное"""
    return a % 2 == 0


def split_into_pairs(a):
    """Разделяет последовательность на пары,
    упаковывая их в двухмерный массив"""
    if not if_even(len(a)):
        return
    if not check_sorted(a):
        return
    i = 0
    some_list = []
    for j in range(int(len(a) / 2)):
        some_list.append([a[i+j], a[i+j+1]])
        i += 1
    return some_list


pupil = [[1594663340, 1594663389,], [1594663390, 1594663395] , [1594663396, 1594666472]]
tutor = [[1594663290, 1594663430, ], [1594663443, 1594666473]]


def interval_by_second(a, limit):
    """"""
    seconds_online = set()
    for i in range(len(a)):
        for sec in range(a[i][0] if a[i][0] > limit[0] else limit[0],
                         a[i][1] if a[i][1] < limit[1] else limit[1]):
            seconds_online.add(sec)
    return seconds_online


def count_seconds_together(a, b):
    interval_together = a.intersection(b)
    return len(interval_together)


print(count_seconds_together(interval_by_second(pupil, lesson), interval_by_second(tutor, lesson)))

# print(split_into_pairs(tutor))


