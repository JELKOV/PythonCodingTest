# 학생 수 입력 받기
# 첫 번째 입력된 값은 학생 수 N개
N = int(input("학생 수를 입력하세요: "))

# 점수를 저장할 리스트 생성
scores = list(map(int, input("점수를 공백으로 구분하여 입력하세요: ").split()))

# 초기 최댓값과 최솟값 설정
max_score = scores[0]
min_score = scores[0]

# 최댓값과 최솟값 찾기
for i in range(1, N):
    if scores[i] > max_score:
        max_score = scores[i]  # 최댓값 갱신
    if scores[i] < min_score:
        min_score = scores[i]  # 최솟값 갱신

# 최댓값과 최솟값의 차이 계산 및 출력
difference = max_score - min_score
print(difference)
