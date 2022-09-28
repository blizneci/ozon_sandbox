"""
Программа для суммирования двух чисел.
В первой строке целое числ - кол-ко наборов входных данных.
Далее описания t наборов входных данных, один набор в строке.
Для каждого набора выведите сумму двух заданных чисел.
"""
import io, os


"""
# Для контеста
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
data = input()
for line in data[1:]:
    line = map(int, line.strip().split())
    print(sum(line))
"""
def check_sum(case, ans):
    case = map(int, case.strip().split())
    ans = int(ans.strip())
    return sum(case) == ans

def main(file_case, file_answer):
    f_case = open(test_path + file_case, 'r')
    f_answer = open(test_path + file_answer, 'r')
    cases: list[str] = f_case.readlines()
    answers: list[str] = f_answer.readlines()
    for i, (case, ans) in enumerate(zip(cases[1:], answers), 1):
        if check_sum(case, ans):
            print(f"Sum of {case.strip()} == {ans.strip()}")
            print(f"Test {i} passed")
        else:
            print(f"Sum of {case.strip()} != {ans.strip()}")
            print(f"Test {i} failed")
            f_case.close()
            f_answer.close()
            break
    else:
        f_case.close()
        f_answer.close()
        print(f"All test cases in file case {file_case} are passed")


test_path = "./tests_sandbox/tests_A/"
file_cases_list = os.listdir(test_path)
file_cases = (file for file in file_cases_list[::2])
file_answers = (file for file in file_cases_list[1::2])
for file_case, file_answer in zip(file_cases, file_answers):
    main(file_case, file_answer)
    q = input("Continue testing? q for quit\n")
    if q == 'q':
        break


