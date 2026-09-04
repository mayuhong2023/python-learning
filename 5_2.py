def count_code(codes):
    counts={}
    for c in codes:
        counts[c]=counts.get(c,0)+1
    return counts
codes=[]
with open("access.log") as f:
    for line in f:
        line=line.strip()
        if not line:
          continue
        parts=line.split()
        code=int(parts[1])
        codes.append(code)
result=count_code(codes)
print(f"总请求数:{len(codes)}")
for code,num in result.items():
    print(f" 状态码{code}:{num} 次")
blocked=result.get(403,0)
print(f"拦截率：{blocked/len(codes):.1%}")
with open("report.txt","w",encoding="utf-8-sig") as f:
    f.write(f"总请求数:{len(codes)}\n")
    for code,num in result.items():
        f.write(f"状态码{code}:{num}次\n")
    f.write(f"拦截率：{blocked/len(codes):.1%}\n")

