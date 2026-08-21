n = int(input())
a = list(map(int, input().split()))

counts = []
for x in a:
  count = 0
  while x % 2 == 0:
    x //= 2
    count += 1
  counts.append(count)
  
print(min(counts))


  
