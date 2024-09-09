import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.read
sys.setrecursionlimit(10**6)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    def update(self, idx, value):
        while idx <= self.n:
            self.tree[idx] += value
            idx += idx & -idx
    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def compress(arr):
    sorted_unique = sorted(set(arr))
    return {val: i + 1 for i, val in enumerate(sorted_unique)}
def main():
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    points = []
    x_coords = []
    y_coords = []
    for i in range(1, n + 1):
        x, y = map(int, data[i].split())
        points.append((x, y))
        x_coords.append(x)
        y_coords.append(y)
    queries = []
    for i in range(n + 1, n + m + 1):
        x1, y1, x2, y2 = map(int, data[i].split())
        queries.append((x1, y1, x2, y2))

    x_compressed = compress(x_coords)
    y_compressed = compress(y_coords)
    max_y = len(y_compressed)

    fenwick = FenwickTree(max_y)
    points.sort()
    answer = []
    query_idx = 0
    for x1, y1, x2, y2 in queries: 
        while query_idx < n and points[query_idx][0] <= x2:
            x, y = points[query_idx]
            fenwick.update(y_compressed[y], 1)
            query_idx += 1


        y1_idx = bisect_left(y_compressed, y1)
        y2_idx = bisect_right(y_compressed, y2)
        answer.append(fenwick.range_query(y1_idx, y2_idx))

    sys.stdout.write("\n".join(map(str, answer)) + "\n")
if __name__ == "__main__":
    main()
