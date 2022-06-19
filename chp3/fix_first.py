def fix_first(s):
    ini = s[0]
    ss = s.replace(ini, "*")
    return ini + ss[1:]
print(fix_first("babble"))