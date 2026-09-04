code=int(input("请输入状态码： "))
if code == 403:
    print("被waf拦截")
elif 200<=code<=299:
    print("正常放行")
elif code >= 500:
    print("后端错误")
else:
    print(f"其他状态码：{code}")