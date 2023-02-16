import requests
headers={'user-agent': 'my-app/0.0.1'}
payload={"wd":"pornhub"}
response =requests.get("http://www.baidu.com",params=payload,headers=headers)
print(response.content)