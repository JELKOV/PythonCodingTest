def solution(N):
    battery_usage = 0  # 총 건전지 사용량

    while N > 0:  # N이 0이 될 때까지 반복
        if N % 2 == 0:  # 현재 위치가 짝수일 경우
            N //= 2  # 순간이동 (거리 절반으로 줄임)
        else:  # 현재 위치가 홀수일 경우
            N -= 1  # 점프 (1 감소)
            battery_usage += 1  # 건전지 사용량 증가

    return battery_usage  # 총 건전지 사용량 반환
