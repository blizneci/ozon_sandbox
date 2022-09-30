"""
D. Отчет.
    Входные данные
    В первой строке задано целое число t (1<=t<=10) - кол-во наборов входных данных
    Каждый набор входных данных состоит из двух строк. В первой строке задано целое
    число n (3<=n<=50000). Во второй заданы n целых чисел a1, a2, ... (1<=ai<=n) - отчет сотрудника.
    Выходные данные
    Для каждого набора входных данных выведите ответ на отдельной строке.
    Если отчет соответствует критерию, выведите YES, иначе NO.
    Критерий
    Каждая задача выполнялась без разрыва по дням.
"""

import io, os, filecmp
from collections import deque


def resolver(line):
    row = deque(line.decode().rstrip().split())
    v = set()
    while row:
        cur = row[0]
        if cur in v:
            break
        v.add(cur)
        while row and cur == row[0]:
            row.popleft()
    if row:
        return 'NO'
    else:
        return 'YES'

test_path = './tests_sandbox/tests_D/'
case_files_list = filter(lambda x: 'a' not in x, os.listdir(test_path))
for case_file in case_files_list:
    fd_c = os.open(test_path + case_file, os.O_RDONLY)
    data = os.read(fd_c, os.fstat(fd_c).st_size).splitlines()[2::2]
    os.close(fd_c)
    with open(test_path + case_file + 'a.a', 'a+') as f:
        for line in data:
            f.write(resolver(line) + '\n')

