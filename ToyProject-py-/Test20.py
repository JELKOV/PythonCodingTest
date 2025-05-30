# 문제 설명
'''
창고 정리
1. 같은 물건 같은 칸으로 정리 (List)
2. 리스트의 이동 -> 반복문
3. 조건에 따른 이동 -> 조건문
'''

# 입출력 관리
'''
input
(1) storage (list) ex) ["pencil", "pencil", "pencil", "book"]
(2) num (list) ex) [2, 4, 3, 1]

-> 변환
clean_storage = []
clean_num = []

output
(1) result (string) : 정리시 가장많은 제품의 수
'''

# 자료구조
'''
리스트
'''

# 흐름 설명
'''
1. 기존 정리되어 있지 않는 storage 리스트를 받는다.
2. 그리고 storage에 있는 값들을 받는다.

그리고 새롭게 정리할 리스트를 만든 후에 거기에 있으면 추가하지 않고, 없으면 추가한다.

1. 그리고 없으면 새롭게 숫자를 clean_num에 넣고 / 숫자가 없으면 clean_num에 추가한다.

2. 그리고 리스트를 돌아서 가장 높은 값의 인덱스를 구한 후에 

3. 
'''


def solution(storage, num):
    clean_storage = []
    clean_num = []

    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])

    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer