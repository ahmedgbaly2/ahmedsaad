import requests
from bs4 import BeautifulSoup  as bss4
import csv
url= requests.get("https://www.amazon.eg/s?bbn=21832982031&rh=n%3A21832982031%2Cp_n_size_browse-bin%3A22080102031&pf_rd_i=21832982031&pf_rd_m=A1ZVRGNO5AYLOV&pf_rd_p=1d1adbba-a177-42f6-8813-09012de66527&pf_rd_r=CF9TM38B6R7VYQY7NFEV&pf_rd_s=merchandised-search-10&pf_rd_t=101&ref=s9_acss_bw_cg_BF1202_2b1_w")

#print(url.text)
soup=bss4(url.text,'lxml')
product_title = soup .findAll('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
#print(product_title )
products = soup.findAll('div',{'class':' s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis s-latency-cf-section s-card-border'})
with open('products.csv','w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product name','price'])

    for product in products:
        title =product.find('h2','a-size-mini a-spacing-none a-color-base s-line-clamp-4').text
        price = product.find('span','a-offscreen').text

        writer.writerow([title, price])
print('done') 