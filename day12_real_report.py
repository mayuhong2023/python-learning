import re,requests
def load_log(path):
    pattern = r'^(\S+) .* "\S+ (\S+) \S+" (\d+)'
    records=[]
    with open(path,encoding="utf-8") as f:
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
    return records
def top_n(counter_dict,n=3):
    return sorted(counter_dict.items(),key=lambda x:x[1],reverse=True)[:n]  
def analyze(records):
    codes, attacker, atk_url = {}, {}, {}
    for ip, code, path in records:                 
        codes[code] = codes.get(code, 0) + 1
        if code == 403:
            attacker[ip] = attacker.get(ip, 0) + 1
            atk_url[path] = atk_url.get(path, 0) + 1 
    blocked = codes.get(403, 0)
    return {                                       
          "total": len(records),                     
          "rate": blocked / len(records),            
          "codes": codes, 
          "top_ip": top_n(attacker),
          "top_path": top_n(atk_url),
      }   
def build_text(stats):
    text = f"WAF 日报\n"
    text += f"总请求: {stats['total']}\n"
    text += f"拦截率: {stats['rate']:.1%}\n"
    text += f"Top攻击IP: {stats['top_ip']}\n"
    text += f"热门路径: {stats['top_path']}\n"
    return text
def send_feishu(text):
    url="飞书webhook地址"
    msg = {
      "msg_type": "text", 
      "content": {"text": text}
    }
    r=requests.post(url,json=msg)
    return r.json() 
def main():
      records = load_log("access.log")
      stats = analyze(records)
      text = build_text(stats)
      print(text)                    
      result = send_feishu(text)     
      print(result)                      
main()                             

            
  