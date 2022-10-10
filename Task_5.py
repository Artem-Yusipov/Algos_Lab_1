n = int(input())
ans = []
current_sum = 0
i = 1
while current_sum + i <= n:
    ans.append(i)
    current_sum += i
    i += 1
if current_sum != n:
    ans[-1] += n - current_sum
print(len(ans))
print(*ans)

