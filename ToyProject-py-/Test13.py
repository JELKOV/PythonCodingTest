# # (1) 문자열 길이 구하기
# s = input()
# print(len(s))

# # (2) 짝수 홀수 구하기
# n = int(input())
# if n % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# #  (3) 1~N까지의 합
# ## 예시 입력 10 -> 1+2+3+4+5+6+7+8+9+10 = 55
# n = int(input())
# sumNum = 0
# for i in range(1, n+1):
#     sumNum += i
# print(sumNum)

# # (4) 리스트에서 특정값 갯수 새기
# fruits = ["apple", "banana", "orange", "grape", "mango"]
# print(fruits.count('apple'))

# # (5) 문자열 뒤집기
# s = input()
# print(s[::-1])

# # (6) 최댓값 구하기
# nums = list(map(int, input().split()))
# print(max(nums))

# # (7) 홀수만 출력
# n = int(input())
# for i in range(1, n+1):
#     if i % 2 == 1:
#         print(i)

# #(8) 평균 점수 구하기
# n = int(input())
# scores = list(map(int, input().split()))
# print(f"평균: {sum(scores)/n:.1f}")

# # (9) 특정 글자수 세기
# # 예시 입력: banana → 출력: 3
# s = input()
# print(s.count('a'))

# [10] 좌표 이동 시뮬레이션
cmds = ['up', 'up', 'left', 'down', 'right', 'right']
x, y = 0, 0
for c in cmds:
    if c == 'up':
        y += 1
    elif c == 'down':
        y -= 1
    elif c == 'left':
        x -= 1
    elif c == 'right':
        x += 1
print((x, y))