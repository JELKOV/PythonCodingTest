"""
# PCCE 기출문제 7번: 버스 LV_0

[1] 문제 설명 요약
    (1) 목표
    - 영진이가 기다리는 마지막 정류장에서 버스에 탈 수 있을지 확인하기 위해 남은 좌석 수를 반환
    (2) 규칙
    - 각 정류장에서 "On"은 승차, "Off"는 하차, "-"는 아무 의미 없음
    (3) 입력 값
    - seat (int): 버스의 좌석 수 (1 ≤ seat ≤ 30)
    - passengers (List[List[str]]): 각 정류장에서의 승하차 기록
        - passengers[i][j] = "On" | "Off" | "-"
        - passengers의 길이 = 정류장 수
    (4) 출력 값
    - 마지막 정류장에서의 남은 좌석 수 (int, 음수일 경우 0으로 처리)
    (5) 예외 처리
    - 좌석이 음수가 되는 경우는 0으로 처리함

[2] 자료구조

    (1) List

[3] 알고리즘

    (1) Basic Simulation:
    - 해당 규칙을 그대로 코드로 시뮬레이션
    - 복잡한 알고리즘 없이도 구현 가능

[4] 흐름 설계

    (1)정류장을 순차적으로 돌면서
    - "ON"은 탑승자 수 증가
    - "OFF"는 탑승자 수 감소 -> 증가와 감소 함수를 만들 필요가 있음

    (2) seat를 기준으로 현재인원보다 많으면 남은좌석 = seat - 현재 인원
"""


# 시간 복잡도 o(n * m)
## n = len(passengers) → 정류장 수 (행)
## m = len(passengers[0]) → 각 정류장의 승객 수
def solution_1 (seat, passengers):
    # 남은 시트 초기화
    remaining_seats = seat
    # 현재 탑승자 인원 초기화
    current_passengers = 0

    # 조건처리
    for station in passengers:
        for status in station:
            if status == "On":
                current_passengers += 1
                remaining_seats -= 1
                print("[솔루션1] 남은좌석(-) ", remaining_seats, "탑승자수(+)", current_passengers)
            elif status == "Off":
                current_passengers -= 1
                remaining_seats += 1  # 수정됨
                print("[솔루션1] 남은좌석(+) ", remaining_seats, "탑승자수(-)", current_passengers)
            else:
                continue

    # 2. seat를 기준으로 현재인원보다 많으면 remaining_seats = 0 (예외 처리)
    if remaining_seats < 0:
        remaining_seats = 0

    # 3 최종 좌석수를 리턴 함
    return remaining_seats


print("솔루션1 남은 좌석 수:", solution_1(5, [["On", "On", "On"], ["Off", "On", "-"], ["Off", "-", "-"]]))
# 결과: 3


# 시간 복잡도 o(n * m)
# "On" / "Off"만 필터링하는 방식
# "-" 제거하고 풀기
# max로 조건문 분기하기
def solution_2(seat, passenger):
    current_passengers = 0
    for station in passenger:
        # 제너레이터 표현식으로 구현 (필요할때 하나씩 뽑아서 씀 메모리 부하 관리)
        for status in (s for s in station if s != "-"):
            current_passengers += 1 if status == "On" else -1
            print("[솔루션2] 탑승자수", current_passengers)
        '''
        status라는 변수에 station의 원소중에 "-"가 아닌것들만 들어갑니다.
        for s in station:
            if s != "-":
                status = s
        '''

    return max(seat - current_passengers, 0)

print("솔루션2 남은 좌석 수:", solution_2(5, [["On", "On", "On"], ["Off", "On", "-"], ["Off", "-", "-"]]))
# 결과: 3

# 시간 복잡도 o(n * m)
# 각 정류장을 문자열 리스트로 순회하며 .count()로 "On"과 "Off"만 센다.
def solution_3(seat, passengers):
    total_on = sum(status.count("On") for status in passengers)
    print("[솔루션3] 증가량", total_on)
    total_off = sum(status.count("Off") for status in passengers)
    print("[솔루션3] 감소량", total_off)
    return max(0, seat - (total_on - total_off))

print("솔루션3 남은 좌석 수:", solution_3(5, [["On", "On", "On"], ["Off", "On", "-"], ["Off", "-", "-"]]))
# 결과: 3