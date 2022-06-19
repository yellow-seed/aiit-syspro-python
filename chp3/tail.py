import os
base = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base, './small.txt')

f = open(filepath, 'r')

list = f.readlines()
list.reverse()
for li in list:
    print(li)


f.close()