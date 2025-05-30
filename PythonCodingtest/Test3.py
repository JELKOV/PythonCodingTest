# 소의 수를 입력받음
N = int(input("소의 수를 입력하세요: "))

# 소들의 키를 저장할 배열
heights = list(map(int, input("소의 키를 입력하세요: ").split()))

count = 0  # 볼 수 있는 소의 수를 누적할 변수
stack = []  # 소들의 키를 저장할 스택 역할의 리스트

# 각 소를 순차적으로 처리
for currentHeight in heights:
    # 스택의 최상단에 있는 소가 현재 소보다 작거나 같은 경우 제거
    while stack and stack[-1] <= currentHeight:
        stack.pop()  # 스택에서 마지막 소 제거
    
    # 스택에 남아 있는 소의 수만큼 현재 소가 볼 수 있음
    count += len(stack)
    
    # 현재 소의 키를 스택에 추가
    stack.append(currentHeight)

# 결과 출력 (모든 소들이 볼 수 있는 소의 수)
print(count)
 