"""
E. Отрезки времени
    Входные данные
    Первая строка содержит одно число t(1<=t<=10) - кол-во отрезков времени.
    В следующих строках следуют описания отрезков.
    Описание отрезка времени в формате HH:MM:SS-HH:MM:SS
    Никаких пробелов. Ни в начале, ни в конце.
    Выходные данные
    Для каждого набора выведите YES, если заданный набор проходит валидацию,
    в противном случае выведите NO
    Валидация отрезков.
    Часы, минуты и секунды заданы корректно (часы от 0 до 23Б минуты и секунды от 0 до 59)
    Левая граница отрезка не позже его правой границы (но границы могут быть равны)
    Никакия пара отрезков не пересекается (даже в граничных моментах времени).
"""
import io, os, bisect
from datetime import datetime


def gen_idxs(data, n_sets, i=1):
    for _ in range(n_sets):
        cnt = int(data[i])
        idx = i + 1
        i = idx + cnt
        yield idx, cnt

def parser(strings_set):
    res = []
    for a_str in strings_set:
        a_str = a_str.decode().rstrip()
        start, end = (map(int, a.split(':')) for a in a_str.split('-'))
        try:
            t_start = datetime(1971, 1, 1, *start)
            t_end = datetime(1971, 1, 1, *end)
            if t_end < t_start:
                raise Exception
        except Exception:
            res.clear()
            break
        bisect.insort(res, (t_start, t_end))
    return res

def is_right_set(res):
    if not res:
        return False
    for i in range(1, len(res)):
        if res[i][0] <= res[i-1][1]:
            return False
    return True

def clean_tmp_files(test_path):
    tmp_files = filter(lambda x: 'a.a' in x, os.listdir(test_path))
    for tmp_file in tmp_files:
        print('Removing file: ', tmp_file)
        os.remove(test_path + tmp_file)

test_path = './tests_sandbox/tests_E/'
case_files_list = filter(lambda x: 'a' not in x, os.listdir(test_path))
clean_tmp_files(test_path)
for case_file in case_files_list:
    print('case file is: ', case_file)
    fd_c = os.open(test_path + case_file, os.O_RDONLY)
    input = io.BytesIO(os.read(fd_c, os.fstat(fd_c).st_size)).readlines
    data = input()
    os.close(fd_c)
    n_sets = int(data[0])
    idxs = gen_idxs(data, n_sets)
    f = open(test_path + case_file + 'a.a', 'a+')
    for idx, cnt in idxs:
        strings_set = (data[i] for i in range(idx, idx + cnt))
        res = parser(strings_set)
        if is_right_set(res):
            f.write('YES\n')
        else:
            f.write('NO\n')
    f.close()


