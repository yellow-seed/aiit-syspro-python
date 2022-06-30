import os
import sys
# 使い方
# python nl.py [引数]
# 引数を入力した場合、その名前のファイルをnl.pyと同じ階層から検索する
# 引数を入力しなかった場合、標準入力を受け付ける

counter = 1
if len(sys.argv) > 1:
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        file_name = sys.argv[1]
        filepath = os.path.join(base, './' + file_name) # pythonファイルと同階層のファイルを検索
        file = open(filepath, "r")
        lines = file.readlines()
        for l in lines:
            if l == "\n": # 改行だけの場合は出力しない
                continue
            print(counter, " ", l)
            counter += 1
    except FileNotFoundError:
        sys.exit("nl: No such file in current directory: " + file_name)
else:
    print("input text.")
    words = sys.stdin # ctrl + Dで入力終了
    lines = words.readlines()
    for l in lines:
        if l == "\n": # 改行だけの場合は出力しない
            continue
        print(counter, " ", l)
        counter += 1