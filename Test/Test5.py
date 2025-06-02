# 사용자 입력을 받음
input_data = input()

# '('를 관리하기 위한 스택 생성
stack = []

# 잘린 쇠막대기의 총 조각 수
result = 0

# 문자열의 각 문자를 순회
for i in range(len(input_data)):
    current_char = input_data[i]  # 현재 문자
    if current_char == '(':  # '('인 경우
        stack.append(current_char)  # 스택에 여는 괄호 추가
    else:  # 닫는 괄호인 경우
        stack.pop()  # 스택에서 여는 괄호 제거
        if input_data[i - 1] == '(':  # 바로 직전 문자가 여는 괄호인 경우 (레이저 발사)
            # 현재 스택 크기만큼 조각 추가
            result += len(stack)
        else:  # 쇠막대기의 끝인 경우
            result += 1  # 하나의 조각 추가

# 최종적으로 잘린 쇠막대기의 총 조각 수 출력
print(result)
