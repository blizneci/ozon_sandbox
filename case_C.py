"""
C. Парное программирование
    Команда:
        1. Первый разработчик в команде тот, кто идет первым в списке;
        2. Ему в пару подбирается такой, что разница их уровней минимальна
        (то есть минимально значение |ai - aj|, где |x| - это модуль x).
        Если катдидатов несколько, то выбирается тот, кто находится раньше в списке.
        3.Эти два разработчика образуют команду и удаляются из списка.
    Входные данные
    Первая строка содержит одно целое число - кол-ко наборов входных данных.
    Первая строка каждого набора содержит одно целое число n (2<=n<=50; n четное) - кол-во разработчиков.
    Вторая строка содержит n целых чисел - уровень мастерства каждого разработчика.
    Выходные данные
    Для каждого набора входных данных выведите n/2 строк, i-я строка должна
    содежать пару чисел - номер первого и второго разработчика в i-команде.
    Выводи пустую строку между выводами для наборавходных данных.
"""
import io, os, filecmp


def contest_resolver(data):
    for row in data:
        line = row.strip().split()
        a_dict = dict(enumerate(map(int, line), 1))
        for _ in range(len(a_dict) // 2):
            first = min(a_dict)
            f_grade = a_dict.pop(first)
            second = min(a_dict, key=lambda x: abs(f_grade - a_dict.get(x)))
            del a_dict[second]
            # a_dict.pop(second)
            print(first, second)
        print()

def test_resolver(data, case, a_dir):
    #print("Inside test_resolver")
    for idx, row in enumerate(data, 1):
        line = row.strip().split()
        a_dict = dict(enumerate(map(int, line), 1))
        for _ in range(len(a_dict) // 2):
            first = min(a_dict)
            f_grade = a_dict.pop(first)
            second = min(a_dict, key=lambda x: abs(f_grade - a_dict.get(x)))
            del a_dict[second]
            # a_dict.pop(second)
            print(first, second, file=open(a_dir + case + '-a.a', 'a'), end='\r\n')
        if idx != len(data):
            print(file=open(a_dir + case + '-a.a', 'a'), end='\r\n')

def check_files(test_dir_path, case_file, ans_file):
    return filecmp.cmp(test_dir_path + case_file + '-a.a', test_dir_path + ans_file, shallow=False)

def get_file_names(a_dir):
    print("Inside get_file_names")
    file_list = os.listdir(a_dir)
    return zip(file_list[::2], file_list[1::2])

def main(contest=False):
    if contest:
        input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
        data = input()[2::2]
        contest_resolver(data)
    else:
        print('Contest flag is False')
        print('Start testing files')
        test_dir_path = './tests_sandbox/tests_C/'
        file_names = get_file_names(test_dir_path)
        for case_file, ans_file in file_names:
            print(f'case file is {case_file}')
            fd_case = os.open(test_dir_path + case_file, os.O_RDONLY)
            input = io.BytesIO(os.read(fd_case, os.fstat(fd_case).st_size)).readlines
            data = input()[2::2]
            test_resolver(data, case_file, test_dir_path)
            if check_files(test_dir_path, case_file, ans_file):
                print(f"Test {case_file} passed")
                os.remove(test_dir_path + case_file + '-a.a')
            else:
                print(f"Test {case_file} failed")
                break

main(contest=False)



