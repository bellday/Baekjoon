def solution(name, yearning, photo):
    answer = []
    name_sum=0
    for p in photo:
        name_sum=0
        for  index, photo_name in enumerate(p):
            #print(index,photo_name)
            if photo_name in name:
                name_sum+=yearning[name.index(photo_name)]
        answer.append(name_sum)
                
    return answer