num=[]
result={}
n=int(input('enter number of values'))
print('Enter values')
for i in range(n):
    v=int(input())
    num.append(v)
print(num)

for i in range(1,10): 
    count=0
    for j in num:
        if j%i==0:  
            count+=1 
    result[i]=count  

print(result)
