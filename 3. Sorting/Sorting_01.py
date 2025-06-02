"""
# [PCCE 기출문제] 10번 / 데이터 분석 LV_1

[1] 문제 설명

    (1) 목표
    - 이차원 리스트 형태의 데이터를 특정 조건(ext 필드 < val_ext)으로 필터링하고,
      주어진 필드(sort_by)를 기준으로 오름차순 정렬하여 결과를 반환한다.

    (2) 규칙
    - ext 필드의 값이 val_ext보다 작은 항목만 필터링
    - sort_by 필드 기준으로 오름차순 정렬
    - 필드명은 문자열로 주어지며, 내부적으로 인덱스로 매핑되어 처리됨

    (3) 입력 값
    - data (List[List[int]]): 각 원소는 [code, date, maximum, remain] 형식의 정수 리스트
    - ext (str): 필터링 기준 필드명 ("code", "date", "maximum", "remain")
    - val_ext (int): 필터링 기준 값 (ext 필드 < val_ext 조건 적용)
    - sort_by (str): 정렬 기준 필드명 ("code", "date", "maximum", "remain")

    (4) 출력 값
    - 조건을 만족한 데이터만 남긴 후, 정렬된 이차원 리스트 (List[List[int]])

    (5) 예외 상황
    - 필터링 후 결과가 비어 있을 수 있음 → 빈 리스트 반환

[2] 자료구조

    - List:
        - data: 입력된 이차원 배열 (레코드 집합)
        - filtered: 조건에 맞는 데이터 저장
        - 각 레코드 자체도 리스트 형태

    - Dictionary:
        - field_index: 문자열 필드명을 인덱스로 변환하기 위한 매핑용 딕셔너리

    - Integer:
        - 비교 기준값 val_ext, 필드별 값 등 비교/정렬 기준으로 사용

[3] 알고리즘

    - Basic Simulation:
        - 필드명을 인덱스로 바꾸고, 해당 조건에 따라 데이터를 필터링 및 정렬함
        - 명시된 규칙을 그대로 구현한 구조

    - Brute Force:
        - 모든 행을 순차적으로 확인하며 조건을 검사함 (O(n))

    - 정렬(Sorting):
        - 필터링된 리스트를 특정 필드 기준으로 `sort()`로 정렬

[4] 흐름 설계

    (1) 입력 처리:
        - data, ext, val_ext, sort_by가 함수 인자로 주어짐

    (2) 초기 상태 정의:
        - field_index 딕셔너리를 통해 필드명 ↔ 인덱스 매핑
        - ext_idx, sort_idx 변수로 인덱스 추출

    (3) 반복/조건 처리 구조:
        - for문을 통해 data의 각 행 d를 순회
        - d[ext_idx] < val_ext 조건을 만족하는 경우만 filtered 리스트에 추가

    (4) 중간 상태 갱신:
        - filtered 리스트에 조건 만족한 행들을 append

    (5) 종료 조건 / 정렬 처리:
        - filtered 리스트를 `sort()` 함수로 정렬
        - key는 sort_by 필드에 해당하는 인덱스

    (6) 출력 반환:
        - 정렬된 filtered 리스트 반환
"""


def solution(data, ext, val_ext, sort_by):
    # 필드명에 대응되는 인덱스 매핑
    field_index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    ext_idx = field_index[ext]
    sort_idx = field_index[sort_by]

    print(f"\n[디버깅] ext 기준: {ext}({ext_idx}), val_ext: {val_ext}")
    print(f"[디버깅] sort 기준: {sort_by}({sort_idx})")

    # 필터링 단계
    filtered = []
    for d in data:
        print(f"→ 원본 데이터: {d}")
        if d[ext_idx] < val_ext:
            print(f" 조건 만족 → 포함됨")
            filtered.append(d)
        else:
            print(f" 조건 불만족 → 제외")

    # 정렬 전 확인
    print(f"\n[디버깅] 필터링 후 데이터 (정렬 전):")
    for row in filtered:
        print(row)

    # 정렬
    filtered.sort(key=lambda x: x[sort_idx])

    # 정렬 후 확인
    print(f"\n[디버깅] 정렬 후 데이터:")
    for row in filtered:
        print(row)

    return filtered


data = [
  [1, 20300104, 100, 80],
  [2, 20300804, 847, 37],
  [3, 20300401, 10, 8]
]
ext = "date"
val_ext = 20300501
sort_by = "remain"

solution(data, ext, val_ext, sort_by)