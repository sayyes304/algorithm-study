# 큰 수의 법칙 (1) 1이 될 때까지

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0  # 연산 횟수

while True:
    # N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n // k) * k
    result += (n - target)  # 1을 빼는 연산 횟수
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)  # 최종 답안 출력
