n= int(input())
fibo = [0,1] # 0,1 
if n ==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    print(fibo[n])