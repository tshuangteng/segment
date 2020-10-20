import requests

# localhost ip: 218.83.245.18

proxies = {
    'http': 'http://183.165.40.120:17315',
    'https': 'https://183.165.40.120:17315',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Connection': 'keep-alive'}

res = requests.get(url='http://httpbin.org/ip', proxies=proxies, headers=headers)
header = requests.get(url='http://httpbin.org/headers', proxies=proxies, headers=headers)

res = res.json()['origin']
headers_json = header.json()['headers']

headers = ''
for k, v in headers_json.items():
    tmp = f'{k}:{v}\n'
    headers += tmp

print(f'此次请求的真实IP： {res}')
print(f'此次请求头信息： \n{headers}')
