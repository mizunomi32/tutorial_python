# 06. ファイルに書かれている文字を標準出力せよ．
#     - bashでいう"cat"コマンドを実装すればよい．
#     - ファイル名は"sample.txt"とプログラム中で指定する

f = open('sample.txt','r')
for i in f.readlines():
    print(i,end="")  
f.close()
