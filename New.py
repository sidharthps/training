import requests
from parsel import Selector
import csv
proxies = {
 'http': 'http://172.16.244.221:20058',
  'https': 'http://172.16.244.221:20058',
 }
headers = {
'Request URL': 'https://www.gsmarena.com/',
'Request Method': 'GET',
'Status Code': '200 OK',
'Remote Address': '148.251.96.211:443',
'Referrer Policy': 'strict-origin-when-cross-origin',
'Connection': 'Upgrade, Keep-Alive',
'Content-Encoding': 'gzip',
'Content-Length': '12204',
'Content-Type': 'text/html; charset=utf-8',
'Date': 'Fri, 23 Apr 2021 06:55:30 GMT',
'Keep-Alive': 'timeout=15, max=100',
'Server': 'Apache',
'Upgrade': 'h2',
'Vary': 'Accept-Encoding',
'X-Powered-By': 'PHP/7.4.13',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '__cfduid=d83032ca8ebede775c92beebc71932d251618896879; _ga=GA1.2.897214147.1618931098; _gid=GA1.2.1940872237.1618931098; sSubmenuState=open; sHistory=10860%2C10742%2C10817%2C10737%2C10850',
'Host': 'www.gsmarena.com',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
Final_Data = []
url = 'https://www.gsmarena.com'
text = requests.get(url,headers=headers,proxies=proxies,timeout=100).text
print(text)
selector = Selector(text=text)
path= selector.xpath('//div[contains(@class,"brandmenu-v2 light l-box clearfix")]')
product_path = path.xpath('.//a/@href').extract()[1:6]
product_url = ['https://www.gsmarena.com/{}'.format(i) for i in product_path ]
#print(product_url)
for product in product_url:
    text = requests.get(product,headers=headers,proxies=proxies,timeout=100).text
    selector = Selector(text=text)
    product_page = selector.xpath("//div/a[contains(@class,'makers')]//li//a/@href").extract()
    print(product_page)
    for prod in product_page:
            #Product_Data(prod)
        text = requests.get(prod, proxies=proxies,headers=headers, timeout=200).text
        selector = Selector(text=text)
        Product_Name = selector.xpath("//h1[@class='specs-phone-name-title']/text()")
        Product_Price = selector.xpath("//td[@data-spec='price']//a/text()")
        Product_Storage = selector.xpath("//td[@data-spec='internalmemory']/text()")
        Product_Network = selector.xpath("//td[@class='nfo']//a[@class='link-network-detail collapse']/text()")
        Product_Url = selector.xpath("//div[@class='specs-photo-main']//a/@href")
        for Item in zip(Product_Name, Product_Price, Product_Storage, Product_Network, Product_Url):
            Data = {
                'Name': Item[0],
                'Price': Item[1],
                'Storage': Item[2],
                'Network': Item[3],
                'URL': Item[4],
                    }
            Final_Data.append(Data)
print(Final_Data)

toCSV = Final_Data
keys = toCSV[0].keys()
with open('Output.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)





