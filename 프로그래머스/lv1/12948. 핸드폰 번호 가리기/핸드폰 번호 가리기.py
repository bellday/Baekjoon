#마지막-4 부터 0까지 -1 만큼 *로 수정
def solution(phone_number):
    star_phone_number=[]
    for num in range(len(phone_number)-4,0,-1):
        star_phone_number.append('*')
    for n in range(len(phone_number)-4,len(phone_number)):
        star_phone_number.append(phone_number[n])
    return ''.join(star_phone_number)