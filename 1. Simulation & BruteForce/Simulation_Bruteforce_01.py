"""
# 수열과 구간 쿼리 3 LV_0

[1] 문제 설명

    (1) 목표:
    - 정수 배열 arr을 쿼리 배열 queries에 따라 지정된 인덱스끼리 값을 swap하여 최종 배열을 반환
    (2) 규칙:
    - 각 query는 [i, j]로 구성되며, arr[i] <-> arr[j]를 교환
    (3) 입력 값:
    - arr: 정수 리스트 (길이 ≤ 1000)
    - queries: 2차원 리스트 (각 쿼리는 [i, j])
    (4) 출력 값:
    - 변경된 arr 리스트
    (5) 예외:
    - i, j는 항상 유효한 인덱스 (0 ≤ i < j < len(arr))로 보장됨

[2] 자료구조

    (1) List

[3] 알고리즘 선택

    (1) Basic Simulation:
    - 규칙을 순서대로 구현
    (2) Brute Force:
    - 모든 쿼리 순회 처리

[4] 흐름 설계
    (1) arr 복사본 answer 생성
    (2) queries를 순회하며 각 [i, j] 쌍에 대해 값을 서로 교환
    (3) 최종적으로 변경된 배열 answer 반환
"""

def solution(arr, queries):
    # arr을 직접 수정하지 않기 위해 복사본(answer)을 생성
    answer = arr.copy()

    # 쿼리 리스트(queries)를 순차적으로 순회하며 각 [i, j]에 대해 swap 처리
    for i, j in queries:
        # 스왑(Swap) 기능
        answer[i], answer[j] = answer[j], answer[i]

    # 최종적으로 변경된 배열 answer를 반환
    return answer