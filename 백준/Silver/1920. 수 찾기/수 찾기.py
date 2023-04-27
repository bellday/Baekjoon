n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
dict_n={}
for i in n_list:
    if i not in dict_n:
        dict_n[i]=1
for j in m_list:
    if j in dict_n:
        print(1)
    else:
        print(0)
