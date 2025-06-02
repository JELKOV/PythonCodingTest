#(1) 문제이해
# 1-1: 목표 금액(100만원)
# 1-2: Start : 일정금액
# 1-3: Before: 70만원 이상 모일때까지
# 1-4: after: 그 이후 100만원 이상이 모일때까지 저축

#(2) 입출력 파악
# Input
# 2-1: Start : 일정금액 (첫달: 저축 70만원 이하)
# 2-2: Before: 70만원 이상 모일때까지
# 2-3: after: 그 이후 100만원 이상이 모일때까지 저축

# Output
# 100만원이 모일때 까지 걸리는 개월 수 Month

#(3) 자료구조
# 반복문 while ( 반복의 횟수 제한이 없음으로)

#(4) 흐름설계
# 4-1: 첫달 저장
# 4-2: 반복문을 통해서 조건 분기 (while)
# 4-3: 조건 종료시 종료

#(5) 예외상황
# 0 ≤ start ≤ 99
# 1 ≤ before ≤ after ≤ 25

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1

while money < 70:
    money += before
    month += 1

while money < 100:
    money += after
    month += 1

print(month)