n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in range(n - m + 1):
    num = sum(arr[i:i + m])
    result.append(num)
print(max(result))