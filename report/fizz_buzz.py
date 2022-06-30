def fb(i):
    # 倍数の数をセットする
    fizz_array = [""] * 3
    buzz_array = [""] * 5
    # 表示したい文字をセットする
    fizz_array[0] = "Fizz"
    buzz_array[0] = "Buzz"
    number = fizz_array[i % len(fizz_array)] + buzz_array[i % len(buzz_array)]
    return number

i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1