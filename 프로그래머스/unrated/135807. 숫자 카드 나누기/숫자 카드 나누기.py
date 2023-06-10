def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]; gcdB = arrayB[0]
    for i in arrayA:
        gcdA = getgcd(gcdA,i)
        
    for j in arrayB:
        gcdB = getgcd(gcdB,j)
        
    for i in range(len(arrayB)):
        if arrayB[i]% gcdA ==0:
            gcdA=1
        if arrayA[i]% gcdB ==0:
            gcdB = 1
    if gcdA == gcdB:
        return 0
    else:
        return max(gcdA,gcdB)


def getgcd(a,b):
    
    left = b%a
    if left == 0:
        return a
    return getgcd(left,a)