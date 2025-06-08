"""
# 문제명 (PCCE10번 기출문제 LV_1)

[1] 문제 설명

    (1) 목표
    - 문제의 최종 목적은 무엇인가?
    : 조건에 맞는 데이터를 뽑아서 정렬한다.

    (2) 규칙
    - 어떤 조건/제약을 만족해야 하는가?
    : val_ext보다  낮은 값
    : 정렬해야한

    (3) 입력 값
    - 어떤 자료형이 주어지는가? (str, list, int 등)
    - data == 2차원 리스트 [[int code, int date, int maximum, int remain]]
    - ext == 뽑아낼 데이터를 의미하는 문자열
    - val_ext == 뽑아낼 정보의 기준 값 ( 기준값보다 낮은것)
    - sort_by == 해당하는 값을 기준으로 오름차순으로 정렬하여 문자열

    (4) 출력 값
    - 어떤 형식의 값을 출력해야 하는가? (정수, 문자열, 리스트 등)
    -

    (5) 예외 상황
    - 문제에 명시되지 않았지만, 발생할 수 있는 이상한 경우가 있는가?
    - 조건을 만족하는 데이터는 항상 한 개 이상 존재한다.

[2] 자료구조

    (1) 사용한 자료구조와 사용 이유
    List: 원본데이터가 리스트 형태
    Dict: 인덱스 맵핑
    List Comprehension: 조건 필터링 시 유용하게

[3] 알고리즘

    (1) 어떤 알고리즘 유형인지 판단
    - Basic Simulation: 규칙 그대로 구현
    - Brute Force: 모든 경우 탐색
    - Greedy: 매 순간 최선 선택
    - Sorting: 정렬 후 처리
    - DP: 중복 계산 줄이기
    - Hash / Dictionary 기반: 빠른 카운팅/매핑
    - Graph / BFS / DFS: 연결 탐색
    - Binary Search: 정렬된 데이터에서 이분 탐색
    - 기타: 특수 구조 (슬라이딩 윈도우, 투포인터 등)

    (2) 사용 이유 및 타당성 설명
    - Basic Simulation
    - Sorting

[4] 흐름 설계

    (1) 입력 처리
    - data: 이중리스트
    - ext, val_ext, sort_by: 문자열 정수
    (2) 초기 상태 정의
    - 필드명 -> 인덱스 변환용 딕셔너리 생성
    (3) 반복/조건 처리 구조
    - data에서 index의 필드명 의 값과 비교해서 만족한 항목만 필터링
    (4) 중간 상태 갱신 또는 저장
    - 필터링된 리스트를 sort_by기준 인덱스로 정렬한다.
    (5) 종료 조건 / 최종 처리
    - 정렬된 리스트를 결과로 반환
    (6) 출력 반환
    - 이중리스트 반환
"""


def solution(data, ext, val_ext, sort_by):
    # (1) 필드명을 index로 매핑
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_idx = idx[ext]
    print(ext_idx)
    sort_idx = idx[sort_by]
    print(sort_idx)

    # 2. 조건에 맞는 데이터 필터링
    filtered = []
    for row in data:
        if row[ext_idx] < val_ext:
            filtered.append(row)
    # 2.1 리스트 컴플리핸션
    # filtered = [row for row in data if row[ext_idx] < val_ext]
    # print(filtered)

    # 3. 정렬 기준에 따라 정렬
    filtered.sort(key=lambda x: x[sort_idx])

    # 4. 결과 반환
    return filtered


data = [
    [1, 20300104, 100, 80],
    [2, 20300804, 847, 37],
    [3, 20300401, 10, 8]
]

ext = "date"           # 필터링 기준: 제조일
val_ext = 20300501     # 20300501 이전인 데이터만 남김
sort_by = "remain"     # 현재 수량(remain) 기준으로 오름차순 정렬

# 함수 호출
result = solution(data, ext, val_ext, sort_by)
print("최종 결과:", result)