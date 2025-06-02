# 문제 이해
'''
1. 주어진 상황
- 각 칸마다 색이 칠해진 2차원 격자 보드판
- 그 중에 한칸을 골랐을때, / 위 아래 오른쪽 왼쪽/ 같은 색깔로 칠해진 칸의 갯수를 구해야 한다. ex) 빨간 4개 , 초록 3개
'''
# 입출력 구조
'''
(1) board: 2차원 문자열 리스트 (각 칸의 칠해진 색깔 이름을 담음)
(2) 고른 칸의 위치를 나타내는 두정 수 h,w ->  h(1차원 리스트) w(2차원 리스트)

return -> count를 리턴 / 칸의 갯수 
'''

# 자료 구조
'''
(1) 2차원 문자열 리스트 board
'''

# 흐름 설계
'''
1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장합니다.
2. 같은 색으로 색칠된 칸의 갯
'''

def solution(board, h, w):
    # [1] 보드의 세로 크기(행 수)를 변수 n에 저장
    n = len(board)

    # [2] 같은 색을 가진 인접 칸의 개수를 저장할 변수 초기화
    count = 0

    # [3] 상, 하, 좌, 우를 탐색하기 위한 방향 리스트 (각각의 인접칸 위치 계산용)
    dh = [0, 1, -1, 0]  # 행 변화량: 오른쪽, 아래, 위, 왼쪽 순
    dw = [1, 0, 0, -1]  # 열 변화량: 오른쪽, 아래, 위, 왼쪽 순

    print(f"기준 위치: ({h}, {w}), 색상: {board[h][w]}")
    print(f"보드 크기: {n} x {len(board[0])}")

    # [4] 4방향(상하좌우)을 순회하며 인접 칸을 확인
    for i in range(4):
        # [4-1] 인접한 칸의 좌표 계산
        h_check = h + dh[i]
        w_check = w + dw[i]
        print(f"\n→ 방향 {i}: 체크 좌표 ({h_check}, {w_check})")

        # [4-2] 보드 범위를 벗어나지 않는지 확인 (인덱스 오류 방지)
        if 0 <= h_check < n and 0 <= w_check < len(board[0]):
            print(f"   - 유효 좌표")
            print(f"   - 이웃 색상: {board[h_check][w_check]}")
            # [4-3] 기준 칸(board[h][w])과 인접 칸의 색상이 같으면 count 증가
            if board[h][w] == board[h_check][w_check]:
                print(f"   - 색 일치 → count +1")
                count += 1
            else:
                print(f"   - 색 다름")
        else:
            print(f"   - 유효하지 않은 좌표")

    print(f"\n최종 count: {count}")
    # [5] 같은 색깔로 칠해진 인접 칸의 총 개수 반환
    return count


board = [
    ["blue", "red", "green"],
    ["red", "red", "blue"],
    ["yellow", "green", "red"]
]
h, w = 0, 1
solution(board, h, w)