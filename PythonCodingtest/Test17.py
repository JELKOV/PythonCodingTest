# (1) 문제 이해
'''
강아지의 이동 경로가 문자열 route로 주어짐
→ 각각의 문자는 방향 이동 (N, S, E, W)
→ 초기 위치 (0, 0)에서 시작
→ 각 방향에 따라 이동하여 최종 좌표 [x, y] 반환
'''

# (2) 입출력 파악
'''
input:
route = "NESWNESW"  # 문자열, 각 문자 = 한 칸 이동

output:
[동쪽 거리, 북쪽 거리] → 1차원 리스트  
예: [2, 3], [-1, -4]
'''

# (3) 자료 구조
'''
x, y 정수 변수	현재 위치 좌표 저장용
for 반복문	문자열 순회
if 조건문	문자에 따라 좌표 변화 적용
'''

# (4) 흐름 설계
'''
초기 좌표 설정: east = 0, north = 0

문자열 route를 하나씩 순회

문자에 따라 좌표값 갱신:

N → north += 1

S → north -= 1

E → east += 1

W → east -= 1

[x, y] 반환
'''

# (5) 예외 상황
'''
1 ≤ route의 길이 ≤ 20
route는 "N", "S", "E", "W"로만 이루어져 있습니다.
'''

def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S":
            north -= 1
        elif i == "E":
            east += 1
        else:
            east -= 1

    return [east, north]

print(solution("NESWNESWWWWWW"))