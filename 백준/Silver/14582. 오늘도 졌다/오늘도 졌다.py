jennymiss = list(map(int, input().split()))
startlink = list(map(int, input().split()))

score_jenny = 0
score_start = 0
win = 0

for i in range(9):
    score_jenny += int(jennymiss[i])
    

    if score_jenny > score_start:
        win += 1  # 제니미스가 승리하고 있음을 알리기 위해사용
    score_start += int(startlink[i])
if score_start > score_jenny and win >= 1:
    print('Yes')
else:
    print('No')
