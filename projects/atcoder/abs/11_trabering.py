N = int(input())

# 直前の時刻と座標（初期値は t=0, x=0, y=0）
prev_t, prev_x, prev_y = 0, 0, 0

can = True

for _ in range(N):
    t, x, y = map(int, input().split())

    # 経過時間 と 移動距離（マンハッタン距離）を計算
    dt = t - prev_t
    dist = abs(x - prev_x) + abs(y - prev_y)

    # 判定条件
    # 1. 距離が時間より長い場合は届かない (dist > dt)
    # 2. 余った時間が偶数でないとピッタリ到着できない ( (dt - dist) % 2 != 0 )
    if dist > dt or (dt - dist) % 2 != 0:
        can = False
        break

    # 次の判定用に現在の値を保存
    prev_t, prev_x, prev_y = t, x, y

if can:
    print("Yes")
else:
    print("No")


'''
考察
理解が追いついていないため、自分のものにできていない
'''
