# 게임 맵 최단거리
"""
알고리즘 / 자료구조
(1) hash
(2) 스택/큐
(3) 힙
(4) 정렬
(5) 완전 탐색
(6) 탐욕법
(7) DP
(8) Graph
(9) 이분탐색
(10) DFS?BFS
"""
#  문제 설명 (자연어)
"""
GRAPH 탐색 / BFS 너비우선탐색 / 큐 자료구조
🎯 목표	시작점 (1,1)에서 종료점 (n,m)까지 최단 거리를 구하기
🚧 룰	0은 벽, 1은 길. 상하좌우로만 이동 가능
🚫 도달 불가능	상대 팀 진영에 갈 수 없다면 -1 반환
📥 입력	2차원 정수 리스트 maps (n행 m열)
📤 출력	int: 최소 칸 수 or -1
"""

# 흐름 설계
'''
(1) 맵 크기 n x m 구하기
(2) 시작 위치: (0, 0), 종료 위치: (n-1, m-1)
(3) 방문 체크용 visited 배열 or 기존 maps 배열 활용
(4) BFS 탐색 시작 → 큐에 (좌표, 거리) 형태로 삽입
(5) 이동할 수 있는 방향: 상, 하, 좌, 우 (dx, dy 배열 활용)
(6) 한 칸씩 이동하며 방문 처리 + 거리 누적
(7) 목표지점 도달 시 → 누적 거리 return
(8) 큐가 끝날 때까지 도달 못하면 → return -1
'''

from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 1))  # (x좌표, y좌표, 이동거리)
    visited[0][0] = True

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    while queue:
        x, y, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가능한 경우