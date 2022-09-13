import io, os


"""
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readlines
data = input()
"""
def sum(pairs):
n = int(data[0])
pairs = (map(int, line.strip().split()) for line in data[1:])
print(*(sum(pair for pair in pairs)), sep='\n', end='\n')



