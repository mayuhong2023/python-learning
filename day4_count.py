def count_codes(codes):
    counts={}
    for c in codes:
        counts[c]=counts.get(c,0)+1
    return counts
codes=[200,403,200,500,403,200,403,404,500,200]
result=count_codes(codes)
print(result)
print(f"总共{len(codes)}条,{len(result)}种状态码")
for code,num in result.items():
   print(f"状态码 {code} 出现 {num} 次")
   
