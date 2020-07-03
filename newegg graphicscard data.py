from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabbing each product: inspect element krke pata chalega every div class for graphics card
containers = page_soup.findAll("div",{"class":"item-container"})
print("Total products: " + len(containers) + "\n")
filename = "products.csv"
f= open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
    brand_class = container.findAll("a",{"class":"item-brand"}) 
    brand = brand_class[0].img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

f.close()