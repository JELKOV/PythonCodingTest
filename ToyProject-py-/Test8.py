#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

#자릿수 분리
#자릿수 합 계산

def solution(N):
    return sum(int(digit) for digit in str(N))

print(solution(123))

def solution(N):
    total = 0
    while N > 0:
        total += N % 10 # 마지막 수 자리 정하기 1의 자릿수 나머지의 값
        N//=10
    return total

print(solution(123))