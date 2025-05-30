def solution(want, number, discount):
    """
    XYZ 마트의 할인 일정에 따라 정현이가 원하는 제품을 모두 구매할 수 있는 회원 등록 가능한 날짜의 총 일수를 계산합니다.

    Parameters:
    want (list): 정현이가 원하는 제품 목록 (문자열 배열)
    number (list): 각 제품별 필요한 수량 (정수 배열)
    discount (list): XYZ 마트의 할인 일정 (문자열 배열)

    Returns:
    int: 회원 등록 가능한 날짜의 총 일수
    """

    # 필요한 제품과 수량을 딕셔너리로 저장합니다.
    # 예: {"banana": 3, "apple": 2, "rice": 2, "pork": 2, "pot": 1}
    target = {want[i]: number[i] for i in range(len(want))}
    
    # 결과를 저장할 변수
    result = 0
    
    # 전체 할인 상품의 길이
    n = len(discount)
    
    # 슬라이딩 윈도우 탐색
    for i in range(n - 9):  # 10일 간격으로 탐색 가능
        # 현재 10일 동안의 상품 목록
        window = discount[i:i+10]
        
        # 현재 윈도우의 상품 빈도를 카운트
        # 예: {"banana": 3, "apple": 2, "rice": 2, "pork": 2, "pot": 1}
        window_count = {}
        for item in window:
            window_count[item] = window_count.get(item, 0) + 1
        
        # 현재 윈도우가 목표 조건을 만족하는지 확인
        if all(window_count.get(key, 0) >= target[key] for key in target):
            result += 1  # 조건 만족 시 회원 등록 가능한 날짜로 카운트
            
    return result
