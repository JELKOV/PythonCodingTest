"""
# PCCE 기출 8번 문제 / 창고정리 LV_0

[1] 문제 설명

    (1) 목표
    - 같은 물건 이름끼리 수량을 합산한 뒤, 가장 많은 수량을 가진 물품 이름을 반환한다.

    (2) 규칙
    - 같은 이름이 여러 번 등장할 수 있고, 수량은 모두 더해져야 한다.
    - 수량이 같으면 먼저 등장한 물품을 우선함 (index 기준)

    (3) 입력 값
    - storage (List[str]) : 물품 이름 리스트 (최대 100개)
    - num (List[int])     : 각 물품의 수량 (storage와 길이 동일)

    (4) 출력 값
    - 가장 많이 보유한 물품 이름 (string)

    (5) 예외 상황
    - 입력은 항상 유효하며, 빈 리스트는 없음

[2] 자료구조 사용

    - List:
        - clean_storage: 고유한 물품 이름 저장
        - clean_num: 각 물품의 누적 수량 저장
        - storage, num 자체도 리스트 형태로 주어짐

    - String:
        - 물품 이름 비교 및 반환에 사용

    - Integer:
        - 수량 누적 및 max 값 비교에 사용

[3] 알고리즘 사용

    - Basic Simulation:
        - 조건(같은 이름 → 수량 합산)을 그대로 구현하는 구조
        - 단순 조건 분기 및 상태 갱신

    - Brute Force:
        - 기존 리스트에서 동일한 물품 이름이 있는지 index 탐색
        - 모든 항목을 순회하며 비교

[4] 흐름 설계

    (1) 입력 처리:
        - storage, num 리스트 입력 받음

    (2) 초기 상태:
        - clean_storage = []
        - clean_num = []

    (3) 핵심 로직:
        - storage를 순회하며
            → 이미 존재하면 수량 누적
            → 없으면 새로 추가

    (4) 중간 상태 갱신:
        - clean_num[idx] += num[i]

    (5) 출력 구성:
        - max(clean_num) 인덱스로 clean_storage에서 이름 추출

    (6) 반환:
        - 최종 물품 이름 반환
"""



def solution(storage, num):
    # 고유한 물품 이름을 저장할 리스트
    clean_storage = []

    # 각 물품 이름에 대응되는 누적 수량을 저장할 리스트
    clean_num = []

    # 입력으로 주어진 storage 리스트를 순회하며
    for i in range(len(storage)):
        # 현재 물품이 clean_storage에 이미 있는 경우 (즉, 이전에 등장한 물품)
        if storage[i] in clean_storage:
            # 해당 물품의 위치(인덱스)를 찾음
            pos = clean_storage.index(storage[i])
            # 같은 인덱스의 clean_num 값을 찾아서 수량을 누적함
            clean_num[pos] += num[i]
        else:
            # 새로운 물품일 경우 이름을 clean_storage에 추가
            clean_storage.append(storage[i])
            # 해당 수량도 clean_num에 함께 추가
            clean_num.append(num[i])

    # 누적된 수량 중 가장 큰 값을 찾음
    max_num = max(clean_num)

    # 가장 큰 수량을 가진 물품의 인덱스를 찾아서
    # 해당 인덱스의 이름을 clean_storage에서 가져옴
    answer = clean_storage[clean_num.index(max_num)]

    # 최종적으로 가장 많이 보유한 물품 이름을 반환
    return answer