import requests
from parsel import Selector
import csv
proxies = {
 'http': 'http://172.16.244.221:20001',
  'https': 'http://172.16.244.221:20001',
 }
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Host': 'www.gsmarena.com',
'Referer': 'https://www.gsmarena.com/samsung-phones-9.php',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
Final_Data = []
url = 'https://www.gsmarena.com'
text = requests.get(url,headers=headers,proxies=proxies,timeout=100).text
selector = Selector(text=text)
path= selector.xpath('//div[contains(@class,"brandmenu-v2 light l-box clearfix")]')
product_path = path.xpath('.//a/@href').extract()[1:6]
product_url = ['https://www.gsmarena.com/{}'.format(i) for i in product_path ]
#print(product_url)
for product in product_url:
    text = requests.get(product,headers=headers,proxies=proxies,timeout=100).text
    selector = Selector(text=text)
    product_page = selector.xpath("//div[contains(@class,'makers')]//a/@href").extract()
    product_data = ['https://www.gsmarena.com/{}'.format(i) for i in product_page]
    #print(product_data)
    for prod in product_data:
        text = requests.get(prod,headers=headers, proxies=proxies, timeout=200).text
        selector = Selector(text=text)
        Product_Name = selector.xpath("//h1[contains(@class,'specs-phone-name-title')]/text()").extract()
        Product_Price = selector.xpath("//td[@data-spec='price']//a/text()").extract()
        Product_Storage = selector.xpath("//td[@data-spec='internalmemory']/text()").extract()
        Product_Network = selector.xpath("//td[@class='nfo']//a[@class='link-network-detail collapse']/text()").extract()
        Product_Url = selector.xpath("//div[@class='specs-photo-main']//a/@href").extract()
        Next_Page = selector.xpath("//a[@class='pages-next']/@href")
        Pages = ['https://www.gsmarena.com/{}'.format(i) for i in Next_Page]
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





