import sys

N = int(input().strip())
if N>=1 and N<101:
    if N%2:
        print ("Weird")
    elif N%2==0:
        if N in range(2,5):
            print("Not weird")
        elif N in range(6,20):
            print ("weird")
        else:
            print ("Not weird")
