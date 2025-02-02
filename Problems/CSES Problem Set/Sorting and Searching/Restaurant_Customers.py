import sys
 
def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    events = []
    idx = 1
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        events.append(a * 2 + 1)  # Evento de inicio (impar)
        events.append(b * 2)      # Evento de fin (par)
        idx += 2
    events.sort()
    max_count = current = 0
    for event in events:
        current += 1 if event % 2 else -1
        if current > max_count:
            max_count = current
    return max_count
 
print(solve())