s, n = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
i = 0
current_sum = 0
while i < len(a) and current_sum + a[i] <= s:
    current_sum += a[i]
    i += 1
print(i)

