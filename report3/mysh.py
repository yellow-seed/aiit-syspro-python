import sys
import os
import subprocess
import shlex

def is_inner_command(args): # 内部コマンドをサポートする
    return args[0] == 'pwd' or args[0] == 'cd'

def command_pwd():
    print(os.getcwd())

def command_cd(args):
    path = os.path.expanduser(args[1])
    try:
        os.chdir(path)
    except:
        print(f'cd: {path}: No such file or directory')

def command_parser(arg): # コマンドを先頭から解釈する
    pipe_divided = arg.split('|') # まずパイプで分割
    command_arr = []
    for c in pipe_divided:
        command_arr.append(shlex.split(c)) # 字句解析はshlexに任せる
    return command_arr

def command_pipe(args): # eg. [[ls, -l], [awk,  '{ x += $5 } END { print (x + 1023) / 1024 "KB" }']]
    buff = []
    for index, command in enumerate(args):
        if index == 0:
            cp0 = subprocess.Popen(
                command,
                stdout=subprocess.PIPE
            )
            buff.append(cp0.stdout)
        elif index + 1 == len(args): # 最終出力
            subprocess.run(
                command,
                stdin=buff[index - 1]
            )
        else:
            cp = subprocess.run(
                command,
                stdout=buff[index - 1]
            )
            buff.append(cp.stdout)


def invoke_subprocess(args): # サイズが1ならただのコマンド 2以上ならパイプしている
    if len(args) > 1:
        command_pipe(args)
    else:
        subprocess.call(args)

is_continue = True

argc = len(sys.argv)
if argc != 1:
    sys.exit("usage: python mysh.py")

while is_continue:
    command = input('mysh> ')
    command_arr = command_parser(command)
    if len(command_arr) == 1: # .eg [[cd ./]]
        arr = command_arr[0]
        if arr[0] == 'exit':
            is_continue = False
        elif is_inner_command(arr):
            if arr[0] == 'cd':
                command_cd(arr)
            elif arr[0] == 'pwd':
                command_pwd()
        else: # 外部コマンドなどを実行
            invoke_subprocess(arr)
    else:
        invoke_subprocess(command_arr)
