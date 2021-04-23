import requests
from lxml.html import fromstring
import csv

proxies = {
 'http': 'http:207.148.109.204:8080',
 }
Final_Data = []
def Parse_Page(url):
    def Product_Data(prod):
        resp = requests.get(prod,proxies=proxies,timeout=100)
        parser = fromstring(resp.text)
        Product_Name = parser.xpath("//h1[@class='specs-phone-name-title']/text()")
        Product_Price = parser.xpath("//td[@data-spec='price']//a/text()")
        Product_Storage = parser.xpath("//td[@data-spec='internalmemory']/text()")
        Product_Network = parser.xpath("//td[@class='nfo']//a[@class='link-network-detail collapse']/text()")
        Product_Url = parser.xpath("//div[@class='specs-photo-main']//a//@href")
        for Item in zip(Product_Name, Product_Price, Product_Storage, Product_Network, Product_Url):
            Data ={
                'Name': Item[0],
                'Price': Item[1],
                'Storage': Item[2],
                'Network': Item[3],
                'URL': Item[4],
                }
            Final_Data.append(Data)
    def Parse_Product(brand):
        resp = requests.get(brand,proxies=proxies,timeout=100)
        parser = fromstring(resp.text)
        Product_List = parser.xpath("///div[@class='makers']//li//a//@href").extract()
        Pr = (f"{brand}/{Product_List}")
        for prod in Pr:
            Product_Data(prod)

    resp = requests.get(url,proxies=proxies,timeout=100)
    print(resp)
    parser = fromstring(resp.text)
    Brand_List = parser.xpath("//div[@class='brandmenu-v2 light l-box clearfix']//li//a//@href")[:5]
    Br = (f"{url}/{Brand_List}")
    # print(Brand_List)
    for brand in Br:
        Parse_Product(brand)
        #print(brand)


Parse_Page('https://www.gsmarena.com')
print(Final_Data)
# toCSV = Final_Data
# keys = toCSV[0].keys()
# with open('Output.csv', 'w', newline='')  as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)




