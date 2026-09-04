codes=[200,403,200,500,403,200,403,404,500,200]
blocked=0
error=0
ok=0
for c in codes:
    if c==403:
        blocked+=1
    if 200<=c<=299:
        ok+=1
    if c>=500:
         error+=1
print(f"共{len(codes)}条，被拦{blocked}条,放行{ok}条，错误{error}条")

      
