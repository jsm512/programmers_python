def solution(a, d, included):
    answer = 0
    tmp = []
    #첫번째 항부터 마지막 항까지 수열 ex) [3,7,11,15,19]
    for i in range(len(included)):
        tmp.append(a + (d * i))
    #included배열에서 True인 idx번호를 가져와 tmp에서 사용 T값만 sum    
    for idx, val in enumerate(included):
        if val:
            answer += tmp[idx]
    return answer
