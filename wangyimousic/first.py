import requests

from wangyimusic.tool import get_params

url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1429392929?csrf_token="
page = 2  # 抓取第几页评论
params = get_params(page)


payload = {'params': params,
           'encSecKey': '257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c'}
files = [

]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
