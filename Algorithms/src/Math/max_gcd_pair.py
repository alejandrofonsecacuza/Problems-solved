from collections import Counter
def max_gcd_pair(arr):
    count = Counter(arr)
    maxi=max(arr)
    for d in range(maxi, 0, -1):
        multiple_count = sum(count[multiple] for multiple in range(d, maxi + 1, d))
        if multiple_count > 1:
            return d
