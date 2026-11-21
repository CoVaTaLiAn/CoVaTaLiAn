# first answer
N, A, B = map(int, input().split())

ans = 0
tot = 0
for n in N:
  ans = sum(int(c) for c in str(N))
  if ans >= A:
    if ans <= B:
      tot += n
print(tot)

# fix 
N, A, B = map(int, input().split())

tot = 0
# 1 から N までの整数を順番にチェック
for n in range(1, N + 1):
    # n の各桁の和を計算
    ans = sum(int(c) for c in str(n))
    
    # 各桁の和が A 以上 B 以下か判定
    if A <= ans <= B:
        tot += n

print(tot)

# shoter opereate time
N, A, B = map(int, input().split())

# 各桁の和を保持する配列を用意
digit_sum = [0] * (N + 1)
tot = 0

for n in range(1, N + 1):
    # O(1) で過去の計算結果を利用
    digit_sum[n] = digit_sum[n // 10] + (n % 10)
    
    if A <= digit_sum[n] <= B:
        tot += n

print(tot)


# fastest
import sys
sys.setrecursionlimit(10**6)

N_str, A, B = input().split()
A, B = int(A), int(B)
L = len(N_str)

memo = {}

def dp(idx, tight, current_sum):
    if current_sum > B:
        return 0, 0
    if idx == L:
        if A <= current_sum <= B:
            return 1, 0  # (条件を満たす個数, 総和)
        return 0, 0

    state = (idx, tight, current_sum)
    if state in memo:
        return memo[state]

    limit = int(N_str[idx]) if tight else 9
    total_cnt = 0
    total_val_sum = 0
    p10 = 10 ** (L - 1 - idx)

    for d in range(limit + 1):
        next_tight = tight and (d == limit)
        cnt, val_sum = dp(idx + 1, next_tight, current_sum + d)
        
        total_cnt += cnt
        total_val_sum += val_sum + d * p10 * cnt

    memo[state] = (total_cnt, total_val_sum)
    return total_cnt, total_val_sum

_, ans = dp(0, True, 0)
print(ans)