# (1) 문제 이해 / 입출력 파악
'''
input
(1) numbers (list) 성적을 문의하려는 학생
(2) our_score 가채점한 점수, 문의하려는 학생 순서
(3) score_list 실제 성적, 번호 순서

output
(1) Same(순서대로 list) 가채점한 점수와 실제성적과 동일하다면 담아서 출력
(2) Different(순서대로 list)에 (다르다면) 담아서 출력
["Same", "Different"]
'''

# (2) 자료 구조
# 반복문

# (3) 흐름 설계 / 예외 상황
'''
1. answer 리스트를 초기화
2. 반복문을 통해 각 학생의 번호를 가져와
   our_score[i]와 score_list[numbers[i] - 1]을 비교
3. 같으면 "Same", 다르면 "Different" 추가
4. answer를 반환

# 예외 상황
- numbers, score_list 모두 유효 범위 내에서 인덱스 접근 가능
- 입력 값 보장이 되어 있어 별도 예외 처리는 필요 없음
'''


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i] - 1]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer