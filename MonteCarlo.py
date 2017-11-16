__author__ = 'kslea_000'
import math
import random
import time

# MontyCarlow

# just use hardcoded n

def monty(n):
    inside = 0
    start = time.time()
    for n in range(0,n):
        x = random.random()
        y = random.random()
        h = math.hypot(x,y)

        if h < 1:
            inside += 1
    end = time.time()
    totalTime = end - start
    s = "n = ", str(n+1) , "pi = ", (4*inside)/n, "time = ", totalTime

    return s


print(monty(10000));
print(monty(100000));
print(monty(1000000));