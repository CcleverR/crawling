import requests
from bs4 import BeautifulSoup

if __name__== "__main__":
    response=requests.get("https://m.news.naver.com/main?mode=LSD&sid1=101")
    #print(response.status_code)
    #print(response.text)


    if response.status_code!=200:
        print("fail to get data")
    else:
        html=response.text
        soup=BeautifulSoup(html,'lxml')
        result=soup.select_one("#ct > div.r_home_wrp._moreViewLinkArea.__persist_content > div.section_headline._cluster_area > div.sh_headline > ul")
        titles =result.select("li > div.sh_headline_text > a")

        i=1
        for title in titles:
            subjectText=title.select_one("strong.sh_headline_text_title").get_text()
            print(i,subjectText)
            i+=1
#ct > div.r_home_wrp._moreViewLinkArea.__persist_content > div.section_headline._cluster_area > div.sh_headline > ul > li:nth-child(1) > div.sh_headline_text