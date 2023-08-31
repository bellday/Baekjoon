import sys
input = sys.stdin.readline
ans=[0 for _ in range(1000001)]
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        ans[j] += i
    ans[i] += ans[i-1]
T=int(input())
for _ in range(T):
    N=int(input())
    print(ans[N])