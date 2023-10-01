def solution(n, arr1, arr2):
    answer = []
    add_str=''
    for num in range(n):#or 구현
        arr = arr1[num] | arr2[num]
        bin_arr=bin(arr)
        bin_arr=bin_arr[2:].zfill(n)
        for string in bin_arr:
            if string =="1":
                add_str+="#"
            elif string =="0":
                add_str+=' '
        answer.append(add_str)
        add_str =''
    return answer