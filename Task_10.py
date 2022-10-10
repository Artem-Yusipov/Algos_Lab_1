n, s = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
ans = []
delete_counter = 0
while delete_counter < len(arr):
    cur_apple = 0
    decrease = 10 ** 10
    increase = -10 ** 10
    for i in range(len(arr)):
        if arr[i] is not None:
            if arr[i][0] <= decrease:
                decrease = arr[i][0]
    for i in range(len(arr)):
        if arr[i] is not None:
            if arr[i][1] >= increase and arr[i][0] == decrease:
                increase = arr[i][1]
                cur_apple = i
    s -= arr[cur_apple][0]
    if s <= 0:
        print(-1)
        break
    s += arr[cur_apple][1]
    ans.append(cur_apple + 1)
    arr[cur_apple] = None
    delete_counter += 1
else:
    print(*ans)

