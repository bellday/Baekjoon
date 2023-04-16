def solution(cacheSize, cities):
    answer = 0
    cache = []
    for index, city in enumerate(cities):
        city = city.lower()
        if city in cache: # cache hit
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
        else: # cache miss
            if cacheSize > 0 and len(cache) >= cacheSize:
                cache.pop(0)
            if cacheSize > 0:
                cache.append(city)
            answer += 5
    return answer