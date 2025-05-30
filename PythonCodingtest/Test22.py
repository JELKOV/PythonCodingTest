# 문제 이해
'''
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
[code, date, maximum, remain]
'''

# 입출력 정리
'''
input
(1) data (list)
(2) ext (String) : 필터링 기준이 되는 필드 이름 (ex: "date")
(3) val_ext (int) : 필터링 기준 값 (예: 20230501 → date < 20230501)
(4) sort_by(String) : 정렬 기준 필드 이름 (예: "remain" → 해당 필드 기준 오름차순 정렬)
'''

# 자료구조 이용
'''
1. 이차원 정수 리스트 data 
'''
# 흐름 설계
'''
1. 각 필드의 인덱스를 정의해둔다:
   code → 0, date → 1, maximum → 2, remain → 3

2. 필터링 단계:
   → ext에 해당하는 필드 값이 val_ext보다 작은 data만 뽑는다

3. 정렬 단계:
   → sort_by에 해당하는 필드를 기준으로 오름차순 정렬

4. 결과 리턴
'''

def solution(data, ext, val_ext, sort_by):
    # 필드명에 대응되는 인덱스 매핑
    field_index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    ext_idx = field_index[ext]
    sort_idx = field_index[sort_by]

    print(f"\n[디버깅] ext 기준: {ext}({ext_idx}), val_ext: {val_ext}")
    print(f"[디버깅] sort 기준: {sort_by}({sort_idx})")

    # 필터링 단계
    filtered = []
    for d in data:
        print(f"→ 원본 데이터: {d}")
        if d[ext_idx] < val_ext:
            print(f"   ✅ 조건 만족 → 포함됨")
            filtered.append(d)
        else:
            print(f"   ❌ 조건 불만족 → 제외")

    # 정렬 전 확인
    print(f"\n[디버깅] 필터링 후 데이터 (정렬 전):")
    for row in filtered:
        print(row)

    # 정렬
    filtered.sort(key=lambda x: x[sort_idx])

    # 정렬 후 확인
    print(f"\n[디버깅] 정렬 후 데이터:")
    for row in filtered:
        print(row)

    return filtered


data = [
  [1, 20300104, 100, 80],
  [2, 20300804, 847, 37],
  [3, 20300401, 10, 8]
]
ext = "date"
val_ext = 20300501
sort_by = "remain"

solution(data, ext, val_ext, sort_by)