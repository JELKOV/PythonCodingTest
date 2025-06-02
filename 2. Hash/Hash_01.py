"""
# 문제명: 완주하지 못한 선수 (Hash or Sorting) LV_1

[1] 문제 설명

    (1) 목표
    - 마라톤에 참가한 선수들 중 한 명이 도중에 완주하지 못했을 때,
      그 선수의 이름을 찾아 반환한다.

    (2) 규칙
    - 참가자 리스트 `participant`, 완주자 리스트 `completion`이 주어짐
    - 단 한 명의 선수가 완주하지 못함
    - 참가자 중 **동명이인**이 있을 수 있음

    (3) 입력 값
    - participant (List[str]): 참가자 이름 리스트 (1 ≤ len ≤ 100,000)
    - completion (List[str]): 완주자 이름 리스트 (participant보다 1명 적음)

    (4) 출력 값
    - 완주하지 못한 선수 이름 (str)

    (5) 예외 상황
    - 이름이 중복될 수 있기 때문에 단순 포함 여부로 비교하면 안 됨

[2] 자료구조

    - List[str]:
        - participant, completion: 이름이 담긴 문자열 리스트

    - Dictionary (collections.Counter 사용 가능):
        - 이름을 key로, 등장 횟수를 value로 저장하여 비교

    - String:
        - 반환할 이름

[3] 알고리즘

    Hash / Counter 방식
    - participant와 completion의 이름 등장 횟수를 비교
    - 차이가 1인 이름이 정답

    Sorting (대체 가능)
    - 두 리스트를 정렬 후 비교
    - 불일치가 발생하는 첫 요소가 정답

[4] 흐름 설계 (Hash 방식 기준)

    (1) participant와 completion을 Counter로 변환하여 등장 횟수 계산

    (2) participant Counter에서 completion Counter를 빼기

    (3) 남은 key가 완주하지 못한 선수의 이름

    (4) 그 이름을 반환
"""

from collections import Counter

def solution(participant, completion):
    p_count = Counter(participant)
    c_count = Counter(completion)
    remain = p_count - c_count  # 차집합 (값이 1인 항목만 남음)
    return list(remain.keys())[0]
