testcase = int(input())
for i in range(testcase):
    n,k = map(int,input().split())
    string  = input()
    dict_num = {}
    string = string*2
    for j in range(n//4):
        s1 = string[j:j+n//4]
        s2 = string [j+n//4: j + n//2]
        s3 = string [j + n//2:j + 3*n//4]
        s4 = string [j + 3*n//4:j+n]
        if int(s1,16) not in dict_num:
            dict_num[int(s1,16)] =1
        if int(s2,16) not in dict_num:
            dict_num[int(s2,16)] =1
        if int(s3,16) not in dict_num:
            dict_num[int(s3,16)] =1
        if int(s4,16) not in dict_num:
            dict_num[int(s4,16)] =1
    num_arr = sorted(dict_num.items(),reverse=True)
    print(f'#{i+1} {num_arr[k-1][0]}')



        








