def fb(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return ''

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1