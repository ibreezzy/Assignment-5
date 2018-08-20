import math
import random
while True:
    a = random.randint(1, 100)
    b = eval(input('Pick any number of your choice: '))
    if a == b:
        print('You are correct!, my secret choice was',a)
    elif abs(a - b) <= 10:
        print('You are close, my secret choice was',a)
    else:
        print('You are not even close. My secret choice was',a, 'Try again')
