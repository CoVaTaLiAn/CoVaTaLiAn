"""
======================================================================
【問題名】: Card Game for Two
【難易度】: ABC-B相当

【問題文】:
N 枚のカードがあります。i 枚目のカードには ai という数が書かれています。
Alice と Bob は、これらのカードを使ってゲームを行います。
ゲームでは、Alice と Bob が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
2 人がすべてのカードを取ったときゲームは終了し、取ったカードの数の合計がその人の得点になります。
2 人とも自分の得点を最大化するように最適な戦略を取った時、Alice は Bob より何点多く取るか求めてください。

【制約】:
- N は 1 以上 100 以下の整数
- ai (1 ≤ i ≤ N) は 1 以上 100 以下の整数

【入力形式】:
N
a1 a2 a3 ... aN

【出力形式】:
両者が最適な戦略を取った時、Alice は Bob より何点多く取るかを出力してください。
======================================================================
"""
# first wrong result
N = int(input())
a = list(map(int, input().split()))

Ali = 0
Bob = 0
a.sort(reverse=True)
for n in range(0, N+1):
  Ali += a[n]
  n += 1
  Bob += a[n]
  
print(abs(Ali - Bob))

# first pass solution
N = int(input())
a = list(map(int, input().split()))

Ali = 0
Bob = 0
a.sort(reverse=True)
for n in range(0, N , 2):
  Ali += a[n]
  if n + 1 < N:
    Bob += a[n + 1]
  
print(abs(Ali - Bob))

# fix solution 
N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

Ali = sum(a[::2])
Bob = sum(a[1::2])
  
print(abs(Ali - Bob))