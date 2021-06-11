import random
print("숫자를 맞춰보세요 (1~100)")
ans = random.randint(1, 100)
i = 0
while i != ans:
    i = int(input())
    if (i < ans):
        print("숫자가 너무 작습니다.")
    elif (i > ans):
        print("숫자가 너무 큽니다.")
    else:
        print(f"정답입니다. 입력한 숫자는 {i}입니다.")

