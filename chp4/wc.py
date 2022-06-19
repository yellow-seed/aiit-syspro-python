import sys

f = sys.stdin
s = f.read()
# end 最後に改行しないために明示的にセット
print(s, file=sys.stdout, end='')