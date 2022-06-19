def first_last(s):
    # ret = s[:2] + s[-2:]
    # ret = s1[0] + s1[1] + s1[-2] + s1[-1]
    # ret = s1[0] + s1[1] + s1[4] + s1[5]
    # ret = s1[0:2] + s1[-2:]
    ret = s1[:2] + s1[-2]
    return ret

s1 = "spring"
s2 = first_last(s1)
print(s2)