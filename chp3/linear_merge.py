def linear_merge(li1, li2):
    li1.extend(li2)
    return sorted(li1)

print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))