# [1] 문제 파악
# 같은 이름의 물건은 이름별로 수량을 합쳐야 함
# 최종적으로 가장 수량이 많은 물건 이름만 리턴

# [2] 자료 구조 결정
# 물건 이름별 개수를 저장해야 하므로 ➝ dict 사용 적합

# [3] 알고리즘 설계 순서
# storage와 num을 동시에 순회
# dict를 만들어서 이름별 개수를 누적

# 가장 큰 값을 가진 key를 max()로 찾기

storage = ["pencil", "pencil", "pencil", "book"]
num = [2, 4, 3, 1]

# 목표
def solution(storage, num):
    counter = {}  # 이름: 총 수량

    for item, count in zip(storage, num):
        if item in counter:
            counter[item] += count
        else:
            counter[item] = count

    # 가장 많은 개수를 가진 물건 이름 반환
    return max(counter, key=counter.get)



print(solution(storage, num))

