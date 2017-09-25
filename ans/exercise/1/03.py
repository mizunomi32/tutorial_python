# 03. FizzBuzzを実装する
#     - 1から標準入力で受け取った整数までの結果を標準出力．
#     - 結果とは，次のように定義される．
#       - その値が3で割り切れるときは"Fizz"
#       - その値が5で割り切れるときは"Buzz"
#       - その値が両方で割り切れるときは"FizzBuzz"
#       - それ以外の場合，その値そのものを出力する．
#     - 入力された整数が6の場合の出力は以下のようになる．
#     	```
# 	    1
# 	    2
# 	    Fizz
#         4
#         Buzz
#         6
#     	```
x = int(input())
for i in range(x):
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print('FizzBuzz')
    elif (i+1) % 3 == 0:
        print('Fizz')
    elif (i+1) % 5 == 0:
        print('Buzz')
    else:
        print(i+1)
