# 06. ファイルに書かれている文字を標準出力せよ．
#     - bashでいう"cat"コマンドを実装すればよい．
#     - ファイル名は"sample.txt"とプログラム中で指定する
f=open('sample.txt','r');print("".join([i for i in f.readlines()]),end="");f.close()
# 84
