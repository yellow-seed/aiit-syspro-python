import sys


def mask_2nd(str):
    chr = str[1]
    word = str.replace(chr, '*')
    word = word[:1] + chr + word[2:]
    print(word)

f = sys.stdin
line = f.readlines()[0]
mask_2nd(line)