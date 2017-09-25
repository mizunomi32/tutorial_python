# 07. 3.で作ったFizzBuzzをファイルに出力せよ．
#     - ファイル名は"fizzbuzz.txt"と固定する．
x = int(input())
f = open('fizzbuzz.txt', 'w')
for i in range(x):
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        f.write('FizzBuzz')
    elif (i+1) % 3 == 0:
        f.write('Fizz')
    elif (i+1) % 5 == 0:
        f.write('Buzz')
    else:
        f.write(str(i+1))
    f.write('\n')
f.close()
