'''
스티커 앞을 찢을 경우 : 맨 뒤를 사용못함
스티커 두번째를 찢을 경우: 첫번째를 사용못함
길이는 1이상 100000이하이기 때문에 1일 경우, 2일 경우에 대한 고려가 필요
'''

def solution(sticker):
    length = len(sticker)
    GainSticker1 = [0] * length
    GainSticker2 = [0] * length
    #길이가 1또는 2일경우 
    if length ==1:
        return sticker[0]
    elif length ==2:
        return max(sticker[0],sticker[1])
    
    
    GainSticker1[0] = sticker[0]
    GainSticker1[1] = max(sticker[0], sticker[1])
    # 스티커 앞을 찢을 경우 , 맨 뒤를 사용 못하기 위해 length -1까지 for문
    for i in range(2,length-1):
        GainSticker1[i] = max(GainSticker1[i-2] + sticker[i],GainSticker1[i-1] )
    
    GainSticker2[0] = 0
    GainSticker2[1] = sticker[1]
    # 스티커 뒤를 찢을 경우, 맨 뒤를 사용할 수 있기 때문에 length 까지 for문 
    for j in range(2,length):
        GainSticker2[j] = max(GainSticker2[j-2] + sticker[j],GainSticker2[j-1] )
    
    return max(max(GainSticker1), max(GainSticker2))