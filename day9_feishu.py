import requests
url="飞书webhook地址"
msg = {
      "msg_type": "text",
      "content": {"text": "测试信息"}
  }   
r=requests.post(url,json=msg)
print(r.status_code)
print(r.json())


