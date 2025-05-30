# 첫 번째 입력: 숫자의 개수 K
K = int(input("숫자의 개수를 입력하세요: "))

# 숫자를 저장할 스택 생성
stack = []

# K개의 숫자 입력 및 처리
for _ in range(K):
    number = int(input("숫자를 입력하세요: "))
    if number == 0 and stack:
        # 숫자가 0이면 스택에서 마지막으로 추가된 숫자 제거
        stack.pop()
    else:
        # 숫자가 0이 아니면 스택에 추가
        stack.append(number)

# 스택에 남아있는 숫자들의 합을 계산
sum_result = sum(stack)

# 최종 결과 출력
print(sum_result)
