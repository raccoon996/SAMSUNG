import sys

sys.stdin = open("input.txt", "r")


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1e9,1e9

def solution():

    def bf(idx, val, add, sub, mul, div):
        global mx,mn
        if idx == N:
            mx = max(mx, val)
            mn = min(mn, val)
            return
        if add:
            bf(idx+1, val+A[idx], add-1, sub, mul, div)
        if sub:
            bf(idx+1, val-A[idx], add, sub-1, mul, div)
        if mul:
            bf(idx+1, val*A[idx], add, sub, mul-1, div)
        if div:
            bf(idx+1, int(val/A[idx]), add, sub, mul, div-1)

    bf(1, A[0], op[0], op[1], op[2], op[3])
    print(mx)
    print(mn)

solution()