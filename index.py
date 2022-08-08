# Import Required Library
from operator import truediv
import requests
import os
from bs4 import BeautifulSoup
import shutil
import json



# Web URL
web_url = "https://viperspin.com"
base_path = 'C:/Users/joker/Desktop/scrap/viperspin'

def DownloadFile2Directory(ppp):
    ppp = ppp.strip()
    p = os.path.basename(ppp)
    dir = ppp.replace(p, '')
    if dir[-1] == '/':
        dir = dir[:-1]
    os.makedirs(base_path + '/' + dir, exist_ok=True)
    # r = requests.get(web_url + url, allow_redirects=True)
    # open(base_path + dir + '/' + p, 'wb').write(r.content)
    r = requests.get(web_url + '/' + ppp, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(base_path + '/' + ppp,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('success to download: ' + ppp)
    else:
        print('failed to download: ' + ppp)
    return True

# Opening JSON file
f = open('games.json',encoding="utf-8")
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['data']['games']: 
    DownloadFile2Directory(i['Image'])      
    #print(i['Image'])    
        
  
# Closing file
f.close()


# # get HTML content
# html = requests.get(web_url).content

# # parse HTML Content
# soup = BeautifulSoup(html, "html.parser")

# js_files = []
# cs_files = []
# img_files = []

# f = open("image_files.txt", "r")
# for url in f:
#     DownloadFile2Directory(url)



# for script in soup.find_all("script"):
#     if script.attrs.get("src"):
#         url = script.attrs.get("src")
#         js_files.append(url)
#         DownloadFile2Directory(url)

# for image in soup.find_all("img"):
#     if image.attrs.get("src"):
#         url = image.attrs.get("src")
#         img_files.append(url)
#         DownloadFile2Directory(url)
        

# for css in soup.find_all("link"):
#     if css.attrs.get("href"):
#         _url = css.attrs.get("href")
#         cs_files.append(_url)
#         DownloadFile2Directory(_url)

# # adding links to the txt files
# with open("javajavascript_files.txt", "w") as f:
#     for js_file in js_files:
#         print(js_file, file=f)

# with open("image_files.txt", "w") as f:
#     for img_file in img_files:
#         print(img_file, file=f)
        

# with open("css_files.txt", "w") as f:
# 	for css_file in cs_files:
# 		print(css_file, file=f)

