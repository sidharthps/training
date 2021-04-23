import requests
from lxml.html import fromstring
import csv
Output = []
def Scrape_Data(URL):
    resp = requests.get(URL)
    parser = fromstring(resp.text)
    Product_Name = parser.xpath("//h2[@class='woocommerce-loop-product__title']/text()")
    Product_Price = parser.xpath("//span[@class='price']//span[@class='woocommerce-Price-amount amount']/text()")
    Product_Url = parser.xpath("//a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']/@href")
    Page_Numbers = parser.xpath("//a[@class='next page-numbers']/@href")

    for Item in zip(Product_Name,Product_Price,Product_Url):
        Data = {
            'Name': Item[0],
            'Price': Item[1],
            'URL': Item[2],
        }
        Output.append(Data)
    #print(Page_Numbers)

    if '/10' in Page_Numbers[0]:
        print("Pagination exceeded")
    else:
        Scrape_Data(Page_Numbers[0])

Scrape_Data('https://scrapeme.live/shop/')
toCSV = Output
keys = toCSV[0].keys()
with open('Output.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)