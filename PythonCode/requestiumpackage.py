from requestium import Session
from bs4 import BeautifulSoup
#创建一个会话对象
s = Session()
#设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
s.headers.update(headers)
#发送GET请求，搜索“学习资料”
response = s.get('https://www.baidu.com/s', params={'wd': '学习资料'})
# 使用BeautifulSoup解析HTML，并提取搜索结果列表
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.select('.result')
#输出搜索结果标题和URL
for result in results:
    title = result.h3.text
    url = result.a['href']
    #发送GET请求，获取重定向后的真实地址
    response = s.get(url)
    real_url = response.url
    print(title)
    print(real_url)
    print()