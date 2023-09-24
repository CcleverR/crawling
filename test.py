import requests
from bs4 import BeautifulSoup

if __name__== "__main__":
    response=requests.get("https://www.inhatc.ac.kr/sites/kr/index.do")
    #print(response.status_code)
    #print(response.text)


    if response.status_code!=200:
        print("fail to get data")
    else:
        html=response.text
        soup=BeautifulSoup(html,'lxml')
        result=soup.select_one("#menu73_obj380 > div._fnctWrap.wrap_notice > ul > li.active > div.list > ul")
        i=1
        titles =result.select("li > div > a")
        for title in titles:
            subjectText=title.select_one("div.subjectText ").get_text()
            content=title.select_one('div.content').get_text()
            print(i,subjectText,content)
            i+=1
