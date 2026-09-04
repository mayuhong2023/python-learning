codes=[200,403,200,500,403,200,403,404,500,200]
blocked=0
error=0
ok=0
other=0
for c in codes:
    if c==403:
        blocked+=1
    elif 200<=c<=299:
        ok+=1
    elif c>=500:
         error+=1
    else:
        other+=1
rate=blocked/len(codes)
print(f"共{len(codes)}条，被拦{blocked}条,放行{ok}条，错误{error}条,其他{other}条")
print(f"拦截率：{rate:.1%}")

      
