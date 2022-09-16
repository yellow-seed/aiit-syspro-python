import sys
import itertools

def has_option(arg):
    return arg == '-c' or arg == '-u' or arg == '-d' or arg == '-i'

def uniq(lines):
    for k, g in itertools.groupby(list(map(lambda l: l.rstrip(), lines))): # 形式 ['aaa', ['aaa', 'aaa']], ['bbb', ['bbb', 'bbb']] ...
        print(k)

def uniq_c(lines):
    for k, g in itertools.groupby(list(map(lambda l: l.rstrip(), lines))):
        print(str(len(list(g))) + ' ' + k)

def uniq_u(lines):
    for k, g in itertools.groupby(list(map(lambda l: l.rstrip(), lines))):
        if len(list(g)) == 1:
            print(k)

def uniq_d(lines):
    for k, g in itertools.groupby(list(map(lambda l: l.rstrip(), lines))):
        if len(list(g)) >= 2:
            print(k)

def uniq_i(lines):
    rstripped_lines = list(map(lambda l: l.rstrip(), lines)) # オリジナルの配列
    index = 0
    print(rstripped_lines[index])
    for k, g in itertools.groupby(list(map(lambda l: l.lower(), rstripped_lines))): # 全て小文字化してグループ化
        index += len(list(g))
        if index < len(rstripped_lines):
          print(rstripped_lines[index]) # グループ化したときの各グループの配列の先頭の値を出力

def uniq_with_option(lines, opt):
    if opt == '-c':
        uniq_c(lines)
    elif opt == '-u':
        uniq_u(lines)
    elif opt == '-d':
        uniq_d(lines)
    elif opt == '-i':
        uniq_i(lines)

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
    lines = f.readlines()
    uniq(lines)
elif argc == 2:
    if has_option(sys.argv[1]):
        option = sys.argv[1]
        f = sys.stdin
        lines = f.readlines()
        uniq_with_option(lines, option)
    else:
        try:
            f = open(sys.argv[1], "r")
            lines = f.readlines()
            uniq(lines)
        except IOError:
            sys.exit("uniq: No such file or directory: {}".format(sys.argv[1]))
elif argc == 3:
    if has_option(sys.argv[1]):
        option = sys.argv[1]
        try:
            f = open(sys.argv[2], "r")
            lines = f.readlines()
            uniq_with_option(lines, option)
        except IOError:
            sys.exit("uniq: No such file or directory: {}".format(sys.argv[2]))
    else:
        try:
            f = open(sys.argv[1], "r")
            lines = f.readlines()
            uniq(lines)
        except IOError:
            sys.exit("uniq: No such file or directory: {}".format(sys.argv[1]))
else:
    sys.exit("usage: python uniq.py [option] [input_file]")

f.close()

