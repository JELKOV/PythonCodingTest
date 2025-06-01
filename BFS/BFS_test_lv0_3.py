"""
# 겹치는 선분의 길이 LV0
[1] 문제 이해
- (1) 선분 3개가 놓여져 있고 겹쳐있는 길이의 합을 리턴한다.
- (2) input->2차원 배열 lines ( 3개의 선의 정보)
- (3) output-> int answer

[2] 자료구조 / 알고리즘
- (1) Hash (dict)	✅ 가능	각 좌표에 선분이 얼마나 겹쳤는지를 dict 또는 배열로 세면 빠름
- (2) Stack / Queue	❌ 불필요	선입선출, 후입선출 필요 없음
- (3) Heap	❌ 불필요	우선순위 개념 없음
- (4) Sorting	❌ 필요 없음	단순 좌표 체크로 해결 가능
- (5) Brute Force Search	✅ 사용됨	좌표 한 칸씩 모두 확인하는 단순 반복 구조
- (6) Greedy	❌ 필요 없음	선택/최적화 개념 없음
- (7) DP	❌ 불필요	이전 결과 저장·활용 구조 아님
- (8) Graph / DFS-BFS	❌ 무관	연결 구조 없음
- (9) Binary Search	❌ 필요 없음	정렬된 리스트 탐색 구조 아님

[3] 흐름 설계
- (1) 전체 좌표를 저장할 배열 생성 (혹은 dict)
- (2) 각 선분의 구간 [start, end) 범위만큼 반복하며 해당 좌표에 1씩 증가
- (3) 겹침이 2 이상인 구간을 모두 더함
"""


# def solution(lines):
#     # 좌표의 범위는 -100 ~ 100이므로 총 201개의 구간을 관리해야 함
#     # count[i]는 좌표 (i - 100) 위치가 선분에 의해 몇 번 포함되었는지를 의미
#     count = [0] * 201  # 인덱스 0 ~ 200 → 좌표 -100 ~ 100
#
#     # 각 선분의 범위를 순회하며 해당 좌표에 포함된 횟수를 기록
#     # 리스트 언팩킹: 반드시 길이가 2인 리스트나 튜플이어야 합니다.
#     for start, end in lines:
#         # 문제 조건에 따라 end는 포함하지 않음 → [start, end)
#         for i in range(start, end):
#             print(start, end)
#             # 좌표 i에 선분이 하나 지났음을 표시
#             # i가 음수일 수 있으므로 +100 보정을 통해 0 이상 인덱스로 맞춤
#             count[i + 100] += 1
#
#     # 겹쳐진 구간의 길이 계산: 선분이 2번 이상 지나간 구간만 셈
#     overlap_length = 0
#     for x in count:
#         if x >= 2:
#             overlap_length += 1
#     print(overlap_length)
#
#     # 최종 결과 반환
#     return overlap_length

def solution(lines):
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
solution(lines)