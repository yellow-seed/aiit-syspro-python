def match_ends(li):
    num = 0
    for word in li:
        if len(word) >= 2 and word[0] == word[-1]:
            num += 1
    return num

print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))