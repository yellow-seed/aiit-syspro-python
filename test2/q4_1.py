def hash(n):
    # 1文字目がなにか
    magnification = 1
    if n[1] in ['a', 'b', 'c', 'd', 'e', 'f']:
        magnification = 5
    # 文字を数値返還
    ordstr = ord(n)
    return ordstr * magnification % 10
