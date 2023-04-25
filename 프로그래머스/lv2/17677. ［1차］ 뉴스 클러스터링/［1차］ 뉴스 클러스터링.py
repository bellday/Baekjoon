#str1,str2 2글자로 나누기
#만약 둘다 없으면 1을 출력하도록 하자
#2글자만드는법 0 - n-1 까지 구현하기
#for 문을 돌면서 글자를 찾는데 만약 2글자 중 한개라도 문자가아니면 패스 
#문자라면 소문자로 추가하기로 하자
# 그다음 계산하기 * 65536
def solution(str1, str2):
    answer = 0
    str1_dict={}
    str2_dict={}
    str1_list=[]
    str2_list=[]
    j_min=0
    j_max=0
    j_maxlist=[]
    for i in range(len(str1)-1):
         if str1[i].isalpha() == True and str1[i+1].isalpha()== True:
                str1_list.append((str1[i]+str1[i+1]).lower())
                
    for j in range(len(str2)-1):
         if str2[j].isalpha() == True and str2[j+1].isalpha()== True:
                str2_list.append((str2[j]+str2[j+1]).lower())
                
    if len(str1_list)==0 and len(str2_list) ==0:
        return 65536
    
    for s in str1_list:
        if s not in str1_dict:
            str1_dict[s]=1
        else:
            str1_dict[s]+=1
    
    for k in str2_list:
        if k not in str2_dict:
            str2_dict[k]=1
        else:
            str2_dict[k]+=1
    print(str1_dict,str2_dict)
    
    #교집합 & 합집합 구하기
    
    for st in str1_dict:
        
        if st in str2_dict:
            j_min+= min(str1_dict[st],str2_dict[st])
            j_max+= max(str1_dict[st],str2_dict[st])
            j_maxlist.append(st)
        else:
            j_max+=str1_dict[st]
    for z in str2_dict:
        
        if z not in j_maxlist:
            j_max+=str2_dict[z]
        
    
    
    
    
    
    return int((j_min/j_max) * 65536)