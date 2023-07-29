def quad(start_x,start_y,size,answer,arr):
    valid_data = arr[start_x][start_y]
    for i in range(start_x,start_x+size):
        for j in range(start_y,start_y+size):
            
            if arr[i][j]!= valid_data: # 다를경우 1/2 해서검사
                size  = size//2
                quad(start_x,start_y,size,answer,arr)
                quad(start_x+size,start_y,size,answer,arr)
                quad(start_x,start_y + size,size,answer,arr)
                quad(start_x +size,start_y+ size,size,answer,arr)
                return
    answer[valid_data] += 1


def solution(arr):
    answer = [0,0] #0의 갯수 1의 갯수
    n= len(arr)
    quad(0,0,n,answer,arr)
    return answer

