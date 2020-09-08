import requests
import lxml.etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
url = 'http://datachart.500.com/ssq/'
res = requests.get(url,headers=headers)
soul = lxml.etree.HTML(res.text)
items = soul.xpath('//*[@id="tdata"]/tr')
for item in items:
    try:
        datenum = item.xpath('./td[@align="center"]/text()')[0]
        red = item.xpath('./td[@class="chartBall01"]/text()')
        blue = item.xpath('./td[@class="chartBall02"]/text()')
        print(datenum,red,blue)
    except:
        pass