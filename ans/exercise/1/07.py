# 07. 3.で作ったFizzBuzzをファイルに出力せよ．
#     - ファイル名は"fizzbuzz.txt"と固定する．
f=open('fizzbuzz.txt','w');f.write("\n".join(["FizzBuzz"if n%15==0 else"Fizz"if n%3==0 else"Buzz"if n%5==0 else str(n) for n in range(1,int(input())+1)]));f.close()
# 164
