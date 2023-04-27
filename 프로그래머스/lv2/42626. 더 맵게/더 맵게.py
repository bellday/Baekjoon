import heapq


def solution(scoville, K):
    answer = 0
    x=min(scoville)
    scoville.sort()
    heapq.heapify(scoville)


    while x<K and len(scoville)>=2:
        x = heapq.heappop(scoville)
        if x >= K:
            break

        y = heapq.heappop(scoville)
        mix = x + (y * 2)
        heapq.heappush(scoville, mix)
        answer += 1
    x = heapq.heappop(scoville)
    if x<K:
        return -1
    else:
        
        return answer