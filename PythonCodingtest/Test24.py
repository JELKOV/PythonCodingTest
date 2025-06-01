# 게임 맵 최단거리
"""
알고리즘 / 자료구조
(1) hash - 해쉬
(2) Stack / Queue - 스택/큐
(3) Heap - 힙
(4) Sorting - 정렬
(5) Brute Force Search - 완전 탐색
(6) Greedy Algorithm - 탐욕법
(7) Dynamic Programming (DP) - 동적 프로그래밍
(8) Graph - 그래프
(9) Binary Search - 이분 탐색
(10) DFS?BFS

빠르게 찾아야 해?	Hash (dict, set)
순서대로 처리해?	Queue, Stack
최댓값/최솟값 빠르게 꺼내야 해?	Heap
정렬이 필요해?	Sorting
모든 경우를 다 해봐야 해?	완전탐색 (Brute Force)
매번 최선 선택이 답이야?	Greedy
이전 결과를 저장해서 써?	DP
연결된 요소들을 탐색해야 해?	Graph + DFS/BFS
정렬된 리스트에서 빠르게 찾아야 해?	Binary Search
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


def solution(maps):
    # [1] 맵의 세로 길이(n)와 가로 길이(m)를 구함
    n = len(maps)         # 예: 5행
    m = len(maps[0])      # 예: 5열

    # [2] 방문 여부를 저장할 2차원 리스트 visited를 생성 (처음엔 모두 방문하지 않음 = False)
    visited = [[False] * m for _ in range(n)]

    # [3] BFS 탐색을 위한 큐를 리스트로 구현 (시작점: (0, 0), 거리 1부터 시작)
    queue = [(0, 0, 1)]  # (x좌표, y좌표, 이동거리)

    # [4] 시작점 (0, 0)은 방문했다고 표시
    visited[0][0] = True

    # [5] 상하좌우 방향으로 이동하기 위한 delta 배열 정의
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우에 따른 x좌표 이동량
    dy = [0, 0, -1, 1]  # 상, 하, 좌, 우에 따른 y좌표 이동량

    # [6] 큐가 빌 때까지 반복 (BFS 탐색)
    while queue:
        # [6-1] 큐의 가장 앞 요소를 꺼내고, 나머지는 다시 queue에 저장 (시간복잡도는 O(n))
        x, y, dist = queue[0]
        queue = queue[1:]

        # [6-2] 현재 위치가 도착지라면, 지금까지의 거리(dist)를 반환
        if x == n - 1 and y == m - 1:
            return dist

        # [6-3] 4방향으로 이동을 시도
        for i in range(4):
            nx = x + dx[i]  # 이동한 후의 x좌표
            ny = y + dy[i]  # 이동한 후의 y좌표

            # [6-4] 새로운 위치가 맵 범위 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # [6-5] 해당 위치가 벽이 아니고(1이어야 함) 아직 방문하지 않은 곳이면
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny, dist + 1))  # 새로운 위치와 이동거리+1을 큐에 추가

    # [7] 큐를 다 돌았는데도 도착점에 도달하지 못했다면 -1 반환 (도달 불가능)
    return -1