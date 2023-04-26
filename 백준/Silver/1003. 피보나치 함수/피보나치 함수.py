test = int(input())

for i in range(test):
    num = int(input())
    zero = [1, 0]
    one = [0, 1]
    if num == 0:
        print(zero[0],end=' ')
        print(one[0])
    elif num == 1:
        print(zero[1], end=' ')
        print(one[1])
    else:
        for j in range(2, num + 1):
            zero_cnt = zero[j - 1] + zero[j - 2]
            one_cnt = one[j - 1] + one[j - 2]
            zero.append(zero_cnt)
            one.append(one_cnt)
        print(zero_cnt,end=' ')
        print(one_cnt)
