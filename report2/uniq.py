import sys

f = sys.stdin
lines = f.readlines()
setarr = sorted(set(lines), key=lines.index)
for l in setarr:
    l = l.rstrip()
    print(l)

f.close()
