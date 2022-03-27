from random import *

num = range(1,46)
num = list(num)

shuffle(num)

win = sample(num,6)

print("이번주 로또 당첨번호는 {0} 입니다.".format(win))