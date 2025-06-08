import random
# 빅 오메가로 1
# 빅 세타 50 (N/2)
# 빅 오 N
findNumber = random.randint(1,101)

for i in range(100):
    if i == findNumber:
        print(i)
        break