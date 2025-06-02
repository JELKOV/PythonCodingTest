"""
# 문자열 바꿔서 찾기 LV_0

[1] 문제 설명

    (1) 목표
    - 주어진 myString에서 모든 "A"를 "B"로, "B"를 "A"로 바꾼 후,
    - 해당 문자열에 패턴 문자열 pat이 포함되어 있는지 확인하여 존재하면 1, 아니면 0을 반환한다.
    (2) 규칙
    - A ↔ B 치환 후 포함 여부를 판단
    - 치환 후 문자열에 pat이 연속 부분 문자열로 존재해야 함
    (3) 입력 값
    - myString (str): 길이 1~100의 문자열, "A" 또는 "B"만 포함
    - pat (str): 길이 1~10의 문자열, "A" 또는 "B"만 포함
    (4) 출력 값
    - 치환된 문자열에 pat이 포함되면 1, 아니면 0

[2] 자료구조

    (1) 문자열(str)
    (2) for문 기반 문자 변환

[3] 알고리즘

    (1) Simulation:
    - A ↔ B 문자 치환
    (2) Brute Force 탐색 방식:
    - pat in result
    (3) Hash 구조 활용:
    - dict 기반 변환

[4] 흐름 설계

    (1) myString의 각 문자를 순회하며 A는 B로, B는 A로 치환
    (2) 치환된 문자열에 pat이 포함되어 있는지 in 연산으로 확인
    (3) 포함 시 1, 포함되지 않으면 0 반환
"""

s = "hello"
print(s[1:4])  # 결과: "ell"


# 문자열 치환 + 중간 변수 방식 (replace 3단계)
def solution(myString, pat):
    # 1단계: "A"를 임시 문자 "X"로 치환
    #       → 그래야 "B"로 바꾸는 과정에서 덮어씌우는 문제를 방지할 수 있음
    converted = myString.replace("A", "X")

    # 2단계: 원래 "B"였던 부분을 "A"로 바꾼다
    converted = converted.replace("B", "A")

    # 3단계: 임시 문자 "X"를 "B"로 바꿔 원래 A→B가 되도록 완성
    converted = converted.replace("X", "B")

    # 4단계: 바뀐 문자열에 pat이 포함되어 있으면 1, 아니면 0 반환
    return 1 if pat in converted else 0

# 리스트로 하나씩 바꾼 뒤 join
def solution_2(myString, pat):
    swapped = []  # 변환된 문자를 저장할 리스트

    for ch in myString:
        if ch == "A":
            swapped.append("B")  # A → B
        else:  # ch == "B"
            swapped.append("A")  # B → A

    # 리스트를 다시 문자열로 결합
    converted = "".join(swapped)

    # 패턴이 포함되는지 여부로 1 또는 0 반환
    return 1 if pat in converted else 0

# 딕셔너리 + 리스트 내포 방식 (가장 간결한 구현)
def solution_3(myString, pat):
    # A → B, B → A로 매핑하는 딕셔너리
    trans = {"A": "B", "B": "A"}

    # 각 문자에 대해 변환된 문자로 바꿔 문자열 생성 (한 줄 내포)
    converted = "".join(trans[ch] for ch in myString)

    # 패턴이 포함되는지 여부를 int로 바로 반환 (True → 1, False → 0)
    return int(pat in converted)