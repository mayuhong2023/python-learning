import re
pattern = r'^(\S+) .* "\S+ (\S+) \S+" (\d+)'
records=[]
with open("access.log") as f:
    for line in f:
        line=line.strip()
        if not line:
              continue
        m = re.search(pattern, line)
        if m:
             ip   = m.group(1)      
             path = m.group(2)      
             code = int(m.group(3)) 
             records.append((ip,code,path))
def top_n(counter_dict,n=3):
    return sorted(counter_dict.items(),key=lambda x:x[1],reverse=True)[:n]
codes, attacker, atk_url = {}, {}, {}
for ip, code, path in records:                 
    codes[code] = codes.get(code, 0) + 1
    if code == 403:
        attacker[ip] = attacker.get(ip, 0) + 1
        atk_url[path] = atk_url.get(path, 0) + 1
print(f"总请求：{len(records)}")
print(f"状态码分布：{codes}")
blocked=codes.get(403,0)
print(f"拦截率:{blocked/len(records):.1%}")
print("top 3 攻击ip:",top_n(attacker))
print("热门攻击路径:",top_n(atk_url))