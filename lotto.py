__author__ = 'Hwankyu'

import random
import time

def lottoNumber():
    s = set()
    while len(s)<6:
        s.add(random.randint(1,45))
    print(s)

for i in range(1,101):
    lottoNumber()
    time.sleep(1)