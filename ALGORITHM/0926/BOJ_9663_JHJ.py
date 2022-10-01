import sys
sys.stdin = open('example_6.text')

def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count


N =int(input())

ans = dfs([0]*N, 0, N)
print(ans)