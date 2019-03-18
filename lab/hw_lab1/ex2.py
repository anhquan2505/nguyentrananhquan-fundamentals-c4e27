from urllib.request import urlopen
from bs4 import  BeautifulSoup 
import pyexcel
from collections import OrderedDict

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
sữa = urlopen(url)

raw_data = sữa.read()
milk_content = raw_data.decode('utf-8')

soup = BeautifulSoup(milk_content, "html.parser")
style = soup.find("div",style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = style.find("table",id="tableContent")
trs= table.find_all("tr")
table_business=[]
for tr in trs:
    tds = tr.find_all("td")
    
    all_key={}
    for i in range(len(tds)):
        if tds[i].string != None:
            if i == 0:
                all_key["danh mục"] = tds[i].string.strip()
            elif i ==1:
                all_key["quý 4-2016"] = tds[i].string.strip()     
            elif i == 2:
                all_key["quý 1-2017"] =tds[i].string.strip()
            elif i == 3:
                all_key["quý 2-2017"] =tds[i].string.strip()
            elif i==4:
                all_key["quý 3-2017"] = tds[i].string.strip()
    if all_key != {}:
        table_business.append(all_key)        
            
print(all_key)
pyexcel.save_as(records=table_business, dest_file_name="hoạt động kinh doanh sữa.xlsx")            



# with  open ("milk.html","wb") as f:
    
#     f.write(raw_data)


