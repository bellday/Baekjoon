#완전탐색 후 sort로 구현한다음
# index 하기
from itertools import product
def solution(word):
    answer = 0
    alpha=['A','E','I','O','U']
    visited=[0,0,0,0,0]
    string=''
    lan=[]
    for i in range(1,6):
        for per in product(alpha,repeat=i):
            lan.append(''.join(per))
    lan.sort()
    return lan.index(word)+1