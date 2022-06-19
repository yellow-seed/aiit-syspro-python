import os, sys
base = os.path.dirname(os.path.abspath(__file__))
args = sys.argv
# TODO: argsのサイズ1ならファイルが指定されていないので標準入力を受け付ける


filepath = os.path.join(base, './small.txt')

f = open(filepath, 'r')

list = f.readlines()
list.reverse()
for li in list:
    print(li)


f.close()