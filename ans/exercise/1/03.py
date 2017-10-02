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
print("\n".join(["FizzBuzz"if n%15==0 else"Fizz"if n%3==0 else"Buzz"if n%5==0 else str(n) for n in range(1,int(input())+1)]))
# 125
