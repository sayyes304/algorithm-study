# 곱하기 혹은 더하기
# *, + 연산자를 넣어 만들어 질 수 있는 가장 큰 수. 모든 연산은 왼쪽에서 부터 순서대로
# 0,1일 경우 + 나머지는 *

str = input()

# 첫 번째 문자를 숫자로 변경하여 대임
result = int(str[0])

for i in range(1, len(str)):
    # 두 수 중에서 하나라도 0 혹은 1인경우 더하기 수행
    num = int(str[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
