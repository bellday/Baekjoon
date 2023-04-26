num1 = int(input())
num2 = input()
sum=0
multi=1
for i in range(len(num2)):
    print(num1*int(num2[len(num2)-i-1]))
    sum+=(num1*int(num2[len(num2)-i-1]))*multi
    multi*=10
print(sum)
