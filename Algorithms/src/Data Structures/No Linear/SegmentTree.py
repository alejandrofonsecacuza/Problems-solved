class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 2 ** (self.n - 1).bit_length()
        self.tree = [0] * (2 * self.size)
        self.tree[self.size:self.size + self.n] = data
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    def query(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res