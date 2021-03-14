"""
pip install requests
pip install BeautifulSoup4
"""
import requests
from bs4 import BeautifulSoup

count = 5
while count:
    # ############################ 向亚马逊发送请求 ############################
    res = requests.get(
        url="https://www.amazon.com/gp/aod/ajax/ref=aod_f_new?qty=1&asin={}&pc=dp&pageno=1&filters=%257B%2522all%2522%253Atrue%252C%2522new%2522%253Atrue%257D".format(
            "B07V2BBMK4"),
        headers={
            "User-Agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
            "pragma": "no-cache",
            "upgrade-insecure-requests": "1",
            "cache-control": "no-cache",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
            "accept-encoding": "gzip, deflate, br",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
    )
    res.close()
    if res.status_code == 200:
        print("成功")
        break
    else:
        print("请求失败")
        count -= 1

# ############################ res.text内容中提取商户和价格 ############################

soup = BeautifulSoup(res.text, 'html.parser')
tag = soup.find(attrs={'id': "aod-offer-list"})
tag_list = tag.find_all(attrs={'id': "aod-offer"})
for tag in tag_list:
    sold_by = tag.find(attrs={'id': "aod-offer-soldBy"}).find('a').text.strip()
    price = tag.find(attrs={'class': "a-offscreen"}).text.strip()
    message = "{}\t\t{}".format(price, sold_by)
    print(message)
