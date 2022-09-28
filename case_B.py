"""
    Акция "купи 3 одинаковых товара и заплати только за два.
    Каждый купленный товар может участвовать лишь в одной акции.
    Акцию можно использовать многократно.
    Входные данные
    В первой строке записано целое число t - кол-во наборов входых данных.
    Далее записаны наборы входных данных.Каждый начинается строкой, которая
    содержит n - кол-во купленных товаров.
    Следующая строка содержит цены.
    Если цены двух товаров одинаковы, то надо считать, что это один и тот товар.
    Выходные данные.
    Выведите t целых чисел - суммы к оплате для каждого из наборов входных данных.
"""
"""
    # Для контеста
    import io, os
    from collections import Counter

    # Первый вариант
    for _ in range(int(input)):
        _ = input()
        a = Counter(map(int, input().split(' ')))
        s = sum(price * count -(count // 3) * price for price, count in a.items())
        print(s)
    # Второй вариант
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
    data = input()[2::2]
    for line in data:
        a = Counter(map(int, line.decode().rstrip().split(' ')))
        s = sum(price * (count - (count // 3)) for price, count in a.items())
        print(s)
"""
import io, os
from collections import Counter


def check(case_data, ans_data):
    for case_line, ans_line in zip(case_data, ans_data):
        a = Counter(map(int, case_line.decode().rstrip().split(' ')))
        s = sum(price * (count - (count // 3)) for price, count in a.items())
        ans = int(ans_line.decode().rstrip())
        if s == ans:
            continue
        else:
            return False
    return True

test_path = './tests_sandbox/tests_B/'
file_list = os.listdir(test_path)
case_files_list = (file for file in file_list[::2])
ans_files_list = (file for file in file_list[1::2])
for i, (case_file, ans_file) in enumerate(zip(case_files_list, ans_files_list), 1):
    case_fd = os.open(test_path + case_file, os.O_RDONLY)
    ans_fd = os.open(test_path + ans_file, os.O_RDONLY)
    case_input = io.BytesIO(os.read(case_fd, os.fstat(case_fd).st_size)).readlines
    ans_input = io.BytesIO(os.read(ans_fd, os.fstat(ans_fd).st_size)).readlines
    case_data = case_input()[2::2]
    ans_data = ans_input()
    os.close(case_fd)
    os.close(ans_fd)
    if check(case_data, ans_data):
        """
        if i != len(file_list) // 2:
            q = input("Continue testing with next test file? q for quit\n")
            if q == 'q':
                print('Exit')
                break
        """
        print(f"Tests in {case_file} file passed")
        continue
    else:
        break
else:
    print("All tests passed")



