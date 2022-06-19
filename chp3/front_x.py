def front_x(x):
    index = 0
    ans = []
    li = sorted(x)

    for i in li:
        if i[0] == 'x':
            ans.insert(index, i)
            index += 1
        else:
            ans.append(i)
    return ans

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))