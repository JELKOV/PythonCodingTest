'''
# 문자열 바꿔서 찾기

# [1] 문제 설명
(1) 목표
문자열 myString에서 "A"는 "B"로, "B"는 "A"로 서로 바꿨을 때
그 바뀐 문자열 안에 pat 문자열이 **포함되는지 여부(1 또는 0)**를 판단
(2) 룰
myString은 오직 문자 "A"와 "B"로만 이루어짐
바꿀 때: "A" → "B" / "B" → "A"
pat 역시 "A"와 "B"로만 구성됨
바꾼 문자열에 pat이 포함되면 1, 아니면 0
(3) 입력 값
myString: 길이 1~100, 문자열 ("A", "B"만 포함)
pat: 길이 1~10, 문자열 ("A", "B"만 포함)
(4) 출력 값
int: 1 또는 0
(5) 예외 상황
없음 (입력 제한이 충분히 명확하므로 예외 처리 필요 없음)


# [2] 자료구조 / 알고리즘의 선택
(1) hash	❌	해시맵 사용 없음, 검색이 단순 포함 여부 (in)
(2) Stack / Queue	❌	문자 순서 조작 필요 없음
(3) Heap	❌	최대/최소 개념 없음
(4) Sorting	❌	정렬할 필요 없음
(5) Brute Force	✅	한 번 바꾼 후 전체 문자열 내에서 pat in result 검사
(6) Greedy	❌	최선 선택 누적 구조 아님
(7) DP	❌	상태 저장/재활용 불필요
(8) Graph / DFS-BFS	❌	노드, 연결 구조 아님
(9) Binary Search	❌	정렬 리스트에서 탐색이 아님

# [3] 흐름 설계
(1) myString의 각 문자 순회하며 변환
"A" → "B", "B" → "A"
(2) 바꾼 문자열에 pat이 포함되는지 검사
(3) 최종 출력
'''

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

# # 리스트로 하나씩 바꾼 뒤 join
# def solution(myString, pat):
#     swapped = []  # 변환된 문자를 저장할 리스트
#
#     for ch in myString:
#         if ch == "A":
#             swapped.append("B")  # A → B
#         else:  # ch == "B"
#             swapped.append("A")  # B → A
#
#     # 리스트를 다시 문자열로 결합
#     converted = "".join(swapped)
#
#     # 패턴이 포함되는지 여부로 1 또는 0 반환
#     return 1 if pat in converted else 0
#
# # 딕셔너리 + 리스트 내포 방식 (가장 간결한 구현)
# def solution(myString, pat):
#     # A → B, B → A로 매핑하는 딕셔너리
#     trans = {"A": "B", "B": "A"}
#
#     # 각 문자에 대해 변환된 문자로 바꿔 문자열 생성 (한 줄 내포)
#     converted = "".join(trans[ch] for ch in myString)
#
#     # 패턴이 포함되는지 여부를 int로 바로 반환 (True → 1, False → 0)
#     return int(pat in converted)