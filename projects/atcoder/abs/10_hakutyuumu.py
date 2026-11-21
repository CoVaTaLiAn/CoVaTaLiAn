# first pass

S = input()

# 4つの単語を反転させる
words = ["dream", "dreamer", "erase", "eraser"]
rev_words = [w[::-1] for w in words]  # ["maerd", "remaerd", "esare", "resare"]

# 文字列 S も反転させる
rev_S = S[::-1]

i = 0
can = True

while i < len(rev_S):
    matched = False
    
    # 反転した単語のどれかに当てはまるかチェック
    for w in rev_words:
        if rev_S[i : i + len(w)] == w:
            matched = True
            i += len(w)  # 当てはまった単語の長さ分だけ進める
            break
            
    # どの単語にも当てはまらなかったら失敗
    if not matched:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")

'''
考察
原理はわかったが自分でコードの作成がまだできていない

'''