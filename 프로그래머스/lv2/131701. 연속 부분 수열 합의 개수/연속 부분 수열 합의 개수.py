def solution(elements):
    answer = 0
    num_set=set()
    element_len=len(elements)
    element=elements*2
    for i in range(element_len):
        for j in range(element_len):
            num_set.add(sum(element[j:j+i+1]))
    return len(num_set)