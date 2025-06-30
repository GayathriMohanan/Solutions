x=int(input('enter a number')) 
a=1
count=0

while(count<x):
    print(a, end=", " if count != x - 1 else "")
    a+=2
    count+=1

    