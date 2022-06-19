import os, re, sys
base = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base, './small.txt')

f = open(filepath, 'r')
pat = 'but'
list = f.readlines()

for li in list:
    match = re.search(pat, li, flags=re.IGNORECASE)
    if match != None:
        print(re.sub(pat, '***' + match.group(0) + '***', li, flags=re.IGNORECASE))

f.close()