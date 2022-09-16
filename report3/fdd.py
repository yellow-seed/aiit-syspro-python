from datetime import datetime
from PIL import Image 
import imagehash 
import sys
import os
import hashlib
import glob

SHA_256_HASH = {}
FILE_SIZE_HASH = {}
IMAGE_HASH = {}
PRINT_DICT = {}

def has_option(arg): # 再帰探索モード -r と 画像一致探索モード -i
    return arg in ['-r', '-i', '-ri', '-ir']

def is_image_file(path):
    return path.endswith('.jpg') or path.endswith('.png')

def fdd_image_glob(paths, is_recursive):
    for path_name in paths:
        files = glob.iglob(f'{path_name}/**', recursive=is_recursive) # リストより高速なiteratorを採用
        for f in files:
            if os.path.isabs(path_name):
                abs_path = f
            else:
                abs_path = os.path.abspath(f)
            if os.path.isfile(abs_path) and is_image_file(abs_path):
                data = open(abs_path, 'rb').read()
                h = hashlib.sha256(data).hexdigest() # ハッシュによる差分チェック
                ih = imagehash.dhash(Image.open(abs_path))
                size = os.path.getsize(abs_path)
                if h in SHA_256_HASH and data == open(SHA_256_HASH[h][0], 'rb').read():
                    SHA_256_HASH[h].append(abs_path)
                elif size in FILE_SIZE_HASH:
                    FILE_SIZE_HASH[size].append(abs_path)
                elif ih in IMAGE_HASH: # 画像探索の場合ImageHashによる画像一致判定も追加
                    IMAGE_HASH[ih].append(abs_path)
                else:
                    SHA_256_HASH[h] = [abs_path]
                    FILE_SIZE_HASH[size] = [abs_path]
                    IMAGE_HASH[ih] = [abs_path]

    print('The following files are same:')
    for paths in list(SHA_256_HASH.values()): # まずハッシュの同一のものを出力
        if len(paths) > 1:
            for p in paths:
                file_size = os.path.getsize(p)
                file_datetime = datetime.fromtimestamp(os.path.getatime(p))
                print(f"- {p} ({file_size} bytes, {file_datetime})")
                PRINT_DICT[p] = p
    for paths in list(FILE_SIZE_HASH.values()):
        if len(paths) > 1:
            for p in paths:
                if not p in PRINT_DICT: # ハッシュの一致で出力されていないファイルに限定する
                    file_size = os.path.getsize(p)
                    file_datetime = datetime.fromtimestamp(os.path.getatime(p))
                    print(f"- {p} ({file_size} bytes, {file_datetime})")

def fdd_glob(paths, is_recursive):
    for path_name in paths:
        files = glob.iglob(f'{path_name}/**', recursive=is_recursive) # リストより高速なiteratorを採用
        for f in files:
            if os.path.isabs(path_name):
                abs_path = f
            else:
                abs_path = os.path.abspath(f)
            if os.path.isfile(abs_path):
                data = open(abs_path, 'rb').read()
                h = hashlib.sha256(data).hexdigest() # ハッシュによる差分チェック
                size = os.path.getsize(abs_path)
                if h in SHA_256_HASH and data == open(SHA_256_HASH[h][0], 'rb').read():
                    SHA_256_HASH[h].append(abs_path)
                elif size in FILE_SIZE_HASH: # ハッシュ値が異なっていてもファイルのサイズが同一なら同一ファイルの可能性を考慮して追加
                    FILE_SIZE_HASH[size].append(abs_path)
                else:
                    SHA_256_HASH[h] = [abs_path]
                    FILE_SIZE_HASH[size] = [abs_path]

    print('The following files are same:')
    for paths in list(SHA_256_HASH.values()): # まずハッシュの同一のものを出力
        if len(paths) > 1:
            for p in paths:
                file_size = os.path.getsize(p)
                file_datetime = datetime.fromtimestamp(os.path.getatime(p))
                print(f"- {p} ({file_size} bytes, {file_datetime})")
                PRINT_DICT[p] = p
    for paths in list(FILE_SIZE_HASH.values()): # 
        if len(paths) > 1:
            for p in paths:
                if not p in PRINT_DICT: # ハッシュの一致で出力されていないファイルに限定する
                    file_size = os.path.getsize(p)
                    file_datetime = datetime.fromtimestamp(os.path.getatime(p))
                    print(f"- {p} ({file_size} bytes, {file_datetime})")
            
argc = len(sys.argv)
if argc == 2: # python fdd.py path
    path = sys.argv[1]
    fdd_glob([path], False)
elif argc >= 3: # python fdd.py [option] path path...
    if has_option(sys.argv[1]):
        recursive_flg = sys.argv[1] in ['-r', '-ri', '-ir']
        image_search_flg = sys.argv[1] in ['-i', '-ri', '-ir']
        if image_search_flg:
            fdd_image_glob(sys.argv[2:], recursive_flg)
        else:
            fdd_glob(sys.argv[2:], recursive_flg)
    else:
        fdd_glob(sys.argv[1:], False)
