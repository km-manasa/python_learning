from array import *

a = array('i', [])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the next value"))
    a.append(x)

print(a)

val=int(input("Enter the value for search"))
k=0
for e in a:
    if e==val:
        print(k)
        break
    k+=1












