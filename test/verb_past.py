def verb_past(str):
    # 現在形と過去形の対応を連想配列でもつ
    last_chr = str[-1]
    past_dict = { 'go': 'went', 'read': 'read' }
    # まず特殊変化する動詞を検索
    # 次に動詞の末尾チェック
    # 末尾によってd edを決定する
    # すでに過去形なら何もしない
    if str in past_dict:
        return past_dict[str]
    elif str in past_dict.values():
        return str
    elif last_chr == 'c':
        return str + 'ked'
    elif last_chr == 'p':
        return str + 'ped'
    elif last_chr == 'e':
        return str + 'd'
    elif last_chr == 'y':
        s = str[:-1]
        return s + 'ied'
    else:
        return str + 'ed'

print(verb_past('go'))