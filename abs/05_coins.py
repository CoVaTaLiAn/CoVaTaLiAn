# 初期合格
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A+1):
  for b in range(B+1):
    for c in range(C+1):
      if 500 * a + 100 * b + 50 * c == X:
        ans += 1
        
print(ans)


# shorter time & memory
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A + 1):
    for b in range(B + 1):
        # 500円玉と100円玉で作った残りの金額
        rem = X - (500 * a + 100 * b)
        
        # 残額が0以上、かつ50円で割り切れ、必要な枚数がC枚以下なら条件達成
        if rem >= 0 and rem % 50 == 0:
            c = rem // 50
            if c <= C:
                ans += 1

print(ans)