s, n = map(int, input().split())
a = list(map(int, input().split()))
k = [1] + [0] * s
new_k = k[:]
for j in range(len(a)):
    for i in range(a[j], s + 1):
        if k[i - a[j]] == 1:
            new_k[i] = 1
    k = new_k[:]
i = s
while k[i] == 0:
    i -= 1
print(i)
