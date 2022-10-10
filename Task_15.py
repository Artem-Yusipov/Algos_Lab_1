import math

s = input()
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]
ep = [[0 for h in range(n)] for k in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 1
for right in range(n):
    for left in range(right, -1, -1):
        if left == right:
            dp[left][right] = 1
        else:
            minimum = math.inf
            mink = -1
            if s[left] == '(' and s[right] == ')' \
                    or s[left] == '[' and s[right] == ']' \
                    or s[left] == '{' and s[right] == '}':
                minimum = dp[left + 1][right - 1]
            for k in range(left, right):
                if minimum > dp[left][k] + dp[k + 1][right]:
                    minimum = dp[left][k] + dp[k + 1][right]
                    mink = k
            dp[left][right] = minimum
            ep[left][right] = mink


def restoring_response(left, right):
    temp = right - left + 1
    if dp[left][right] == temp:
        return
    if dp[left][right] == 0:
        print(s[left:right + 1], end="")
        return
    if ep[left][right] == -1:
        print(s[left], end="")
        restoring_response(left + 1, right - 1)
        print(s[right], end="")
        return
    restoring_response(left, ep[left][right])
    restoring_response(ep[left][right] + 1, right)


restoring_response(0, n - 1)


