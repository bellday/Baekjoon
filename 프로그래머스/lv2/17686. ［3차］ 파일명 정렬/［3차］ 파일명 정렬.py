def solution(files):
    sort_arr = []
    head, number, tail = '', '', ''
    
    for file in files:  
        head, number, tail = '', '', ''
        for key,val in enumerate(file):
            if file[key].isdigit():     
                head = file[:key]
                number = file[key:]
                
                for j in range(len(number)):    
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                sort_arr.append([head, number, tail])
                
                break

    sort_arr = sorted(sort_arr, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in sort_arr]