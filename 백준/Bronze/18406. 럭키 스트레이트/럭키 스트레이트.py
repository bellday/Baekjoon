def check(N):
    sum_left =0
    sum_right=0
    len_N = len(N)
    for i in range(len_N):
        if i< len_N//2:
            sum_left += int(N[i])
        else:
            sum_right += int(N[i])
    if sum_left == sum_right:
        print("LUCKY")
    else:
        print("READY")
    
N = input()

check(N)
