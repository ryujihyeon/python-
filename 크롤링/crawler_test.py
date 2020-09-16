'''
---------크롤링의 방법----------
원하는 웹페이지에 접속 -> html 데이터를 분석한다 
받아온 html 데이터를 분석가능한 형채로 가공한다 -> 원하는 데이터를 추출한다. 
'''

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get("https://www.naver.com")
# print(response.html.links)

response = requests.get("http://www.naver.com")  #-> requests 라이브러리를 이용했을때  
# print(response.status_code)
# print(response.headers)
# print(response.text)
bs =BeautifulSoup(response.text, "html.parser")
# html parser를 통해, response.text 분석 
for img in bs.select("img") :
    print(img)

for a in bs.select("a"):
    print(a)