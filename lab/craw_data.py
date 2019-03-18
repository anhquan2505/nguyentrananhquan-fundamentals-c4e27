from urllib.request import urlopen
from bs4 import  BeautifulSoup 
import pyexcel
from collections import OrderedDict
        # tạo connection
url = "https://dantri.com.vn"
conn = urlopen(url)



        # download page 
raw_data = conn.read()
html_content = raw_data.decode('utf-8')


with  open ("dantri.html","wb") as f:
    # tên file,wide binary as <shortage>
    f.write(raw_data)
# # print(html_content)
# # (decode:đưa hết về một quy chuẩn)
#         # tìm ROI
# soup = BeautifulSoup(html_content, "html.parser")
# ul = soup.find("ul","ul1 ulnew")
# # riêng vs thẻ class thì k cần viết nhưng vs thẻ id thì phải viết đầy đủ id=""

# # sự khác nhau giữa find và find_all: 

# # for li in li_list:
# # print(a.prettify())
#     # print("*"*50)
     
# # ul.prettify: prettify
#         # phân giải Roi
# li_list = ul.find_all("li")
# # li= li_list[0]
# # h4= li.h4
# # a=h4.a
# # title = a.string
# # link = a["href"]
# # print("title:",title.lstrip())
# # print("link: ", link)
#         # lưu data

# ls=[]
# for li in li_list:
#     # dictionary={}
#     h4= li.h4
#     a=h4.a
#     title= a.string
#     link= url + a["href"]
    
#     dictionary=OrderedDict({
#     "title": title.lstrip().rstrip(),
#     "link": link
#     })
#     ls.append(dictionary)
# print(ls)
# # print('*'*5)

# pyexcel.save_as(records=ls, dest_file_name="dantri_html.xlsx")