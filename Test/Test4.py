def main():
    N = int(input())  # 탑의 개수를 입력받음
    heights = list(map(int, input().split()))  # 각 탑의 높이를 저장할 리스트
    result = []  # 결과를 저장할 리스트

    stack = []  # 탑의 인덱스를 저장할 스택

    # 모든 탑을 순회하면서 수신할 수 있는 탑을 찾음
    for i in range(N):
        # 현재 탑보다 낮은 탑이 스택에 존재하는 경우 제거 (현재 탑이 수신 신호를 가림)
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()  # 스택의 최상단에 있는 탑을 제거 (현재 탑이 해당 탑을 가림)

        # 스택이 비어있으면 수신할 수 있는 탑이 없음
        if not stack:
            result.append(0)  # 0을 결과에 추가 (수신 가능한 탑이 없음)
        else:
            # 스택의 최상단에 있는 탑이 신호를 수신할 수 있는 탑
            # 1-based 인덱스이므로 +1을 더함
            result.append(stack[-1] + 1)

        # 현재 탑의 인덱스를 스택에 추가
        stack.append(i)  # 현재 탑의 위치를 스택에 저장 (다음 탑들의 비교를 위해)

    # 결과 출력
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
