# WIP (DP?)
N, K = map(int, input().split())


n_1type, n_2types, n_3types = 0

if K % 2:
    # 1type (a==b==c)
    n_1type = N // K
else:
    # 1type (a==b==c)
    n_1type = N // (K//2)

# 2types (a==b!=c)
n_2types = (N//K) ** 2 - n_1type  # remove a==b==c patters

# 3types (a!=b!=c)
# ?
