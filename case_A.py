import io, os


"""
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
data = input()
"""
tests_path = 'tests_sandbox/tests_A'
file_list = os.listdir(tests_path)
tests_list = file_list[::2]
answer_list = file_list[1::2]
print('files: ', file_list)
print('test files are: ', tests_list)
print('answer files are: ', answer_list)


