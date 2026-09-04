while True:
    s=input("状态码(输入q退出):")
    if s=="q":
        break
    code=int(s)
    if  code==403:
        print("被waf拦截")
    else:
        print("放行")