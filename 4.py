codes=[200,403,200,500,403,200]
counts={}
for c in codes:
    counts[c]=counts.get(c,0)+1
print(counts)

