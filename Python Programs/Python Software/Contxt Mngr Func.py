from contextlib import contextmanager


def open_file(file,mode):
    f = open(file,mode)
    return f
    f.close()

with open_file('Test.txt','w') as f:
    f.write(input(":"))

print(f.closed)
