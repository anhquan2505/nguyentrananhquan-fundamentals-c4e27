from urllib.request import urlopen
from bs4 import  BeautifulSoup 
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
opens = urlopen(url)

raw_data = opens.read()
html_content = raw_data.decode('utf-8')

soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section","section chart-grid")
div = section.find("div","section-content")
ul = div.find("ul")

li_list = ul.find_all("li")

ls=[]
for li in li_list:
    h3 = li.h3
    h4 = li.h4
    singer= h4.string
    song= h3.string
    dictionary={
    "song": song.lstrip().rstrip(),
    "singer": singer
    }
    ls.append(dictionary)
# print(ls)
# pyexcel.save_as(records=ls, dest_file_name="itune_top_songs.xlsx")

keyls = []
for i in ls:
    key= i["song"] + " " + i["singer"]
    keyls.append(key)
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': len(keyls) # Tell downloader to download only the first entry (video)
}



dl = YoutubeDL(options)
dl.download(keyls)


