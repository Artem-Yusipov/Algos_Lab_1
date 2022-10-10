num = input()
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))
first_arr.sort()
second_arr.sort()
ans = 0
for i in range(len(first_arr)):
    ans += first_arr[i] * second_arr[i]
print(ans)

