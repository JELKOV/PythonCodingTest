# 문제 이해:
# 한국 나이 (현재연도 - 출생연도 +1)
# 연나이 (현재연도 - 출생연도)

# 입출력 파악:
# input: year(int) age_type(str)
# output: 나이(int)

# 자료 구조:
# 없음

# 흐름 설계:
# 출생연도를 입력
# age_type에 따라서 조건 분기
# 2030년도를 기준으로 나이 계산
# 결과 출력

# 예외 상황:
# year는 1950 ~ 2030 으로 보장됨
# age_type은 Korea 또는 Year로 고정됨 -> 추가 검증이 필요가 없음


year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)