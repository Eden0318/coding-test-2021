def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    answer = 0
    for x in win_nums:
        if x in lottos:
            answer += 1
            
    return rank[cnt_0 + answer],rank[answer]