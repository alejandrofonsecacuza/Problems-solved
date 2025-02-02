def solve():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    pr = [[0] * (n + 1) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            pr[i][j + 1] = pr[i][j] + a[i][n - 1 - j]

    ans = -1
    mx = n

    for id in range(mx):
        cnt = 0
        for i in range(n):
            if pr[i][id] == id:
                cnt += 1
        
        if cnt != 0:
            ans = id
        
        mx = min(mx, id + cnt)

    print(ans + 1)
t=int(input())
for _ in range(t):
    solve()
