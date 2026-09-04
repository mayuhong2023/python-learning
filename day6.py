def load_log(path):
    records=[]
    with open(path,encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            ip,code,url=line.split()
            records.append((ip,int(code),url))
    return records
def top_n(counter_dict,n=3):
    return sorted(counter_dict.items(),key=lambda x:x[1],reverse=True)[:n]
records=load_log("access2.log")
codes,attacker,atk_url={},{},{}
for ip,code,url in records:
    codes[code]=codes.get(code,0)+1
    if code==403:
        attacker[ip]=attacker.get(ip,0)+1
        atk_url[url]=atk_url.get(url,0)+1
print(f"总请求：{len(records)}")
print(f"状态码分布：{codes}")
blocked=codes.get(403,0)
print(f"拦截率:{blocked/len(records):.1%}")
print("top 3 攻击ip:",top_n(attacker))
print("热门攻击路径:",top_n(atk_url))