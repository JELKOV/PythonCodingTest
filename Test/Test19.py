# 문제 설명
'''
1. 가습기 문제
- mode_type (auto / target/ minimum)
- (1) auto
    :   0 <= humidity < 10 5단계
    :   10 <= humidity < 20 4단계
    :   20 <= humidity < 30 3단계
    :   30 <= humidity < 40 2단계
    :   40 <= humidity < 50 1단계
    :   50 <= humidity 0단계
- (2) target
    :  humidty < val_set 3단계
    :  humidty > val_set 1단계
- (3) minimum
    : humidity < val_set 1단계
    : humidity > val_set 0단계
'''

# 입력값
'''
input
(1) mode_type (str)
(2) humidity (int)
(3) val_set (int)
'''

def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5

def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer