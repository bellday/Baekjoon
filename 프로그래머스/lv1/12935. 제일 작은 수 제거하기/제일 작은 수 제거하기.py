def solution(arr):
    a= min(arr)
    arr.pop(arr.index(a))
    if len(arr)==0:
        return [-1]
    else:
        return arr