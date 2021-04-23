import requests
from parsel import Selector
from lxml.html import fromstring
import csv
proxies = {
 'http': 'http://172.16.244.221:20001',
  'https': 'https://172.16.244.221:20001',
 }
Final_Data = []

#def Parse_Page(url):
resp = requests.get('https://www.gsmarena.com/',proxies=proxies)
parser = fromstring(resp.text)
Brand_List = parser.xpath("//div[@class='brandmenu-v2 light l-box clearfix']//li//a//@href")[:5]
print(Brand_List)
for brand in Brand_List:
    #Parse_Product(brand)
    resp = requests.get(brand)
    parser = fromstring(resp.text)
    Product_List = parser.xpath("///div[@class='makers']//li//a//@href").extract()

    for prod in Product_List:
            #Product_Data(prod)
        resp = requests.get(prod)
        parser = fromstring(resp.text)
        Product_Name = parser.xpath("//h1[@class='specs-phone-name-title']/text()")
        Product_Price = parser.xpath("//td[@data-spec='price']//a/text()")
        Product_Storage = parser.xpath("//td[@data-spec='internalmemory']/text()")
        Product_Network = parser.xpath("//td[@class='nfo']//a[@class='link-network-detail collapse']/text()")
        Product_Url = parser.xpath("//div[@class='specs-photo-main']//a/@href")
        for Item in zip(Product_Name, Product_Price, Product_Storage, Product_Network, Product_Url):
            Data = {
                'Name': Item[0],
                'Price': Item[1],
                'Storage': Item[2],
                'Network': Item[3],
                'URL': Item[4],
                    }
            Final_Data.append(Data)



#Parse_Page('https://www.gsmarena.com')
# toCSV = Final_Data
# keys = toCSV[0].keys()
# with open('Output.csv', 'w', newline='')  as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)




