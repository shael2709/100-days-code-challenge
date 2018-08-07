from random import randint as r
while True:
     a=r(0,100)
     b=r(0,100)
     print("enter the sum")
     print(a," + ",b,"= ")
     print("Correct" if int(input())== a+b else "Try Again")
