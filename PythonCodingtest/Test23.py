'''
# 문제 설명
 1. 입출력 ( myString) (pat)
 ex) "AABBAB" -> "BABBBA"

 2. output: 부분 문자열 중 pat이 있으면 1 아니면 0
'''

s = "hello"
print(s[1:4])  # 결과: "ell"


def solution(myString, pat):
    # 1단계: A ↔ B 교환
    converted = myString.replace("A", "X").replace("B", "A").replace("X", "B")

    # 2단계: pat이 포함되는지 확인
    return 1 if pat in converted else 0


def solution(myString, pat):
    swapped = []
    for ch in myString:
        if ch == "A":
            swapped.append("B")
        else:  # ch == "B"
            swapped.append("A")
    converted = "".join(swapped)
    return 1 if pat in converted else 0

def solution(myString, pat):
    trans = {"A": "B", "B": "A"}
    converted = "".join(trans[ch] for ch in myString)
    return int(pat in converted)