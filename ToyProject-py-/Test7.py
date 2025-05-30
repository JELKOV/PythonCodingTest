# 양꼬치 계산
# 양꼬치 1인분에 12,000원
# 총가격 = n * 12000

# 음료수 계산
# 음료수 한잔 2,000원 -> 서비스 고려 (10인분당 음료수 한잔)
# max(k - (n // 10), 0)
def solution(n, k):
    # 양꼬치 총 가격
    lamb_price = n * 12000
    # 유료 음료수 계산
    paid_drinks = max(k - (n // 10), 0)
    drink_price = paid_drinks * 2000
    # 총 가격 계산
    total_price = lamb_price + drink_price
    return total_price