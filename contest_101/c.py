# WIP (Two test caces remains WA, The fucking code)
import sys
sys_input = sys.stdin.readline

N, K = map(int, sys_input().split())
AAA = list(map(int, sys_input().split()))

if N == K:
    print(1)
    exit()

n_remain = N
n_calc = 0
while n_remain > 0:
    n_remain += (-K+1)
    n_calc += 1

print(n_calc)
