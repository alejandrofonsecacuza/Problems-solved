def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def solve():
    n, m = cinline()    
    s = input().strip()
    
    # Initialize the grid and row/column sum arow_arrayays
    a = [[0] * (m + 1) for _ in range(n + 1)]
    row_array = [0] * (n + 1) 
    col_array = [0] * (m + 1) 
    
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, m + 1):
            a[i][j] = row[j - 1]
            row_array[i] += a[i][j]
            col_array[j] += a[i][j]
    
    l, r = 1, 1
    
    
    for move in s:
        if move == 'D':  
            tmp = -row_array[l]  
            a[l][r] = tmp
            row_array[l] = tmp + a[l][r] 
            col_array[r] += tmp 
            l += 1 
        else:  
            tmp = -col_array[r]  
            a[l][r] = tmp 
            col_array[r] = tmp + a[l][r]  
            row_array[l] += tmp  
            r += 1
    a[n][m] = -col_array[m]
    
    for i in range(1, n + 1):
        print(' '.join(map(str, a[i][1:m+1])))


    
t=1
t=cinint()
for _ in range(t):
    (solve())