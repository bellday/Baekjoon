def solution(book_time):
    answer = 0
    end_time =[]
    book_time.sort()
    cnt=0
    for book  in book_time:
        start_time = int(book[0][:2])* 60 +int(book[0][3:])
        cnt=0
        if len(end_time)==0:
            end_time.append(int(book[1][:2])*60 +int(book[1][3:]) +10)
        else:
            end_time.sort(reverse = True)
            
            #print(end_time)
            for end in range(len(end_time)):
                if start_time >=end_time[end]:
                    cnt+=1
                    end_time[end] = int(book[1][:2])*60 +int(book[1][3:]) +10
                    break
            if cnt ==0:
                end_time.append(int(book[1][:2])*60 +int(book[1][3:]) +10)
    print(end_time)
                
        
    
    return len(end_time)