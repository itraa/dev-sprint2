# Enter your answrs for chapter 7 here
# Name:Aarthi Narayan
import math

# Ex. 7.5

def fact(k):
    if k == 0:
        return 1
    else:
        return k * fact(k-1)

def estimate_pi():
    k = 0
    summation = 0
    while True:
        sum =  (fact(4 * k) * (1103 + 26390 * k)) / ((fact(k)**4) * 396**(4*k)) 
        summation = sum + summation
        if sum < 1e-15
            break
        k = k + 1

    return 1/((2 * math.sqrt(2)/9801) * summation)

print estimate_pi()
#print math.pi
# How many iterations does it take to converge?
Two iterations