def f(n):
    arr = [[0 for _ in range(n+1)] for _ in range(10)]
    mod = 10 ** 9
    for i in range(10):
        arr[i][1] = 1
    for num in range(2, n + 1):
        for k in range(10):
            match k:
                case 0:
                    arr[0][num] = (arr[4][num - 1] + arr[6][num - 1]) % mod
                case 1:
                    arr[1][num] = (arr[6][num - 1] + arr[8][num - 1]) % mod
                case 2:
                    arr[2][num] = (arr[9][num - 1] + arr[7][num - 1]) % mod
                case 3:
                    arr[3][num] = (arr[8][num - 1] + arr[4][num - 1]) % mod
                case 4:
                    arr[4][num] = (arr[0][num - 1] + arr[3][num - 1] + arr[9][num - 1]) % mod
                case 6:
                    arr[6][num] = (arr[0][num - 1] + arr[1][num - 1] + arr[7][num - 1]) % mod
                case 7:
                    arr[7][num] = (arr[6][num - 1] + arr[2][num - 1]) % mod
                case 8:
                    arr[8][num] = (arr[1][num - 1] + arr[3][num - 1]) % mod
                case 9:
                    arr[9][num] = (arr[2][num - 1] + arr[4][num - 1]) % mod
    sum = 0
    for j in range(1, 10):
        if j != 8:
            sum = (sum + arr[j][n]) % mod
    return sum