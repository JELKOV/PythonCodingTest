### N의 시간 복잡도

N = 100000
cnt = 1

for i in range(N):
    print("연산횟수" + str(cnt))
    cnt += 1

### 3N의 시간 복잡도

N = 100000
cnt = 1

for i in range(N):
    print("연산횟수" + str(cnt))
    cnt += 1

for i in range(N):
    print("연산횟수" + str(cnt))
    cnt += 1

for i in range(N):
    print("연산횟수" + str(cnt))
    cnt += 1

### N2의 시간복잡도

N = 100000
cnt = 1
for i in range(N):
    for j in range(N):
        print("연산횟수" + str(cnt))
        cnt += 1