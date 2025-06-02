"""
# 겹치는 선분의 길이 LV_0

[1] 문제 설명

    (1) 목표
    - 3개의 선분 중 2개 이상이 겹치는 구간의 총 길이를 계산하여 반환한다.
    (2) 규칙
    - 선분 [start, end]는 start ≤ x < end 범위이며 끝점은 포함되지 않음
    - 좌표는 -100 ~ 100의 정수이며, 정수 단위로 선분이 표현됨
    - 한 좌표에 2개 이상 선분이 겹치면 그 구간은 길이 1로 계산됨
    (3) 입력 값
    - lines (List[List[int]]): 3개의 선분 구간 (각 원소는 [a, b])
    - 각 선분은 [a, b] 형태이며, -100 ≤ a < b ≤ 100
    (4) 출력 값
    - 두 선분 이상이 겹치는 구간의 전체 길이 (int)

[2] 자료구조

    (1) List:
    - 카운팅용 배열 201칸

[3] 알고리즘

    (1) Simulation:
    - 선분을 하나씩 순회하며 규칙대로 count 배열에 값을 누적함 (명시된 동작을 그대로 구현)
    (2) Brute Force:
    - 전체 좌표(-100~100)를 모두 순회하며 중복 카운트 확인 / 모든 좌표를 순회하며 값이 2 이상인 key만 필터링
    (3) Hash / Dictionary:
    - 기반 처리: 각 좌표를 Key로 하여 등장 횟수를 기록 (O(1) 삽입/탐색)

[4] 흐름 설계

    (1)  좌표값 -100 ~ 100 범위를 표현하는 카운팅 배열 생성 (길이 201)
    (2)  각 선분의 구간을 순회하며 해당 좌표의 값 +1 처리
    (3)  최종적으로 카운팅 배열에서 값이 2 이상인 칸의 개수를 합산하여 반환
"""

# 고정 크기 배열
# 전체 201개 순회
# O(3 × K) = O(K)
def solution(lines):
    # 좌표의 범위는 -100 ~ 100이므로 총 201개의 구간을 관리해야 함
    # count[i]는 좌표 (i - 100) 위치가 선분에 의해 몇 번 포함되었는지를 의미
    count = [0] * 201  # 인덱스 0 ~ 200 → 좌표 -100 ~ 100

    # 각 선분의 범위를 순회하며 해당 좌표에 포함된 횟수를 기록
    # 리스트 언팩킹: 반드시 길이가 2인 리스트나 튜플이어야 합니다.
    for start, end in lines: # 3번 반복
        # 문제 조건에 따라 end는 포함하지 않음 → [start, end)
        for i in range(start, end):
            print(start, end)
            # 좌표 i에 선분이 하나 지났음을 표시
            # i가 음수일 수 있으므로 +100 보정을 통해 0 이상 인덱스로 맞춤
            count[i + 100] += 1

    # 겹쳐진 구간의 길이 계산: 선분이 2번 이상 지나간 구간만 셈
    overlap_length = 0
    for x in count:
        if x >= 2:
            overlap_length += 1
    print(overlap_length)

    # 최종 결과 반환
    return overlap_length

lines = [[0, 2], [-3, -1], [-2, 1]]
solution(lines)


# 딕셔너리 기반
# O(K + M) ≈ O(K)
def solution_1(lines):
    # 좌표별로 겹친 횟수를 기록할 딕셔너리
    point_map = {}

    print(" 각 선분의 좌표 처리 현황:")
    for start, end in lines:
        print(f"➤ 선분: [{start}, {end})")
        for i in range(start, end):
            # 해당 좌표의 카운트를 1 증가 (기존값이 없으면 0)
            point_map[i] = point_map.get(i, 0) + 1
            print(f"  - 좌표 {i}: {point_map[i]}회")

    print("\n 최종 좌표별 겹친 횟수:")
    for key in sorted(point_map):
        print(f"좌표 {key}: {point_map[key]}회")

    # 2개 이상 선분이 겹친 좌표만 카운트
    overlap_coords = [key for key, val in point_map.items() if val >= 2]
    print("\n2개 이상 겹친 좌표 목록:", overlap_coords)
    print(" 겹친 구간의 총 길이:", len(overlap_coords))

    return len(overlap_coords)

lines = [[0, 2], [-3, -1], [-2, 1]]
solution_1(lines)