# skill_tree에서 요소 한개씩 받아온다. 
# 단어가 없을 수 있다 이 부분에 대해서 예외처리가 필요하다.
# cnt 가 0이면 answer 에 1 추가
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        cnt=0
        num_list=[0]
        for s in skill:
            # 스킬 트리 요소 추가
            num= num_list.pop()
            if s in tree:
                num_list.append(tree.index(s))
            else:
                num_list.append(100)
            if num >num_list[0]:
                cnt+=1
        if cnt ==0:
            answer+=1
            
    return answer