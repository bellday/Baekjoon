def solution(line):
    answer = []
    rst_x =[]; rst_y = []
    cnt =0 
    for i in range(len(line) -1):
        x1 =line[i][0]; y1 = line[i][1] ; num1 = line[i][2]
        for j in range(i+1, len(line)):
            x2 = line[j][0]; y2 = line[j][1]; num2 = line[j][2]
            cnt+=1
            if (x1* y2) - (y1* x2) ==0:
                
                continue
            else:
                
                x= ((y1*num2) - (num1 * y2))/((x1* y2) - (y1* x2))
                y = ((num1 * x2)-(x1*num2))/((x1* y2) - (y1* x2))
                #print(x,y)
                if x == int(x) and y == int(y):
                    rst_x.append(x)
                    rst_y.append(y)
    max_x = int(max(rst_x))
    min_x = int(min(rst_x))
    max_y = int(max(rst_y))
    min_y = int(min(rst_y))
    graph = [['.' for i in range(min_x, max_x+1)] for _ in range(min_y, max_y+1) ]
    
    for r in range(len(rst_x)):
        x=  int(rst_x[r]) - min_x
        y = abs(int(rst_y[r]) - max_y)
        graph[y][x] = '*'
    for i in range(len(graph)):
        a =''.join(graph[i])
        answer.append(a)
    return answer