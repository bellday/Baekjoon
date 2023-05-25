from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_weight = 0
    queue = deque((truck_weights))
    load = [0] * bridge_length
    trucks = deque((load))
    while queue:
        answer += 1
        moved = trucks.popleft()
        sum_weight -= moved
        if sum_weight+queue[0] <= weight:
            truck = queue.popleft()
            trucks.append(truck)
            sum_weight += truck
        else:
            trucks.append(0)
        
    while trucks:
        answer+=1
        trucks.popleft()
    return answer
#a=solution(10,100,[10]	)
#print((a))