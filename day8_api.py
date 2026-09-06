import requests
r=requests.get("https://api.github.com/repos/mayuhong2023/python-learning")
if r.status_code==200:
    data=r.json()
    print(f'仓库名：{data["full_name"]}')
    print(f'star数:{data["stargazers_count"]}')
    print(f'语言：{data["language"]}')
else:
    print(f"请求失败，状态码：{r.status_code}")
    



