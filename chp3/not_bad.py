import re

def not_bad(s):
    ss = re.sub(r'not.*bad', 'good', s)
    return ss

print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad'))
print(not_bad('This tea is not hot'))