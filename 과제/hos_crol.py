import requests
from bs4 import BeautifulSoup


class Doctor:

    def __init__(self, name, major, Specialization) -> None:
        self.name = None



if __name__== "__main__":
    response=requests.get("https://www.inha.com/page/department/medicine/doctor")

    if response.status_code!=200:
        print("fail to get data")
    else:
        html=response.text
        soup=BeautifulSoup(html,'lxml')
        ul=soup.select_one("#doctorForm > div.contents > ul")
        profiles=ul.select("li > a > p.dept > span")
        info_names=ul.select("li > a > p.name")
        info_Specializations=ul.select(" li > a > p.text01")  
        #doctorForm > div.contents > ul > li:nth-child(1) > a > p.text01
        
        for i in range(len(profiles)):
            print(i+1,profiles[i].get_text())
        for i in range(len(info_names)):
            print(i+1,info_names[i].get_text())
        for i in range(len(info_Specializations)):
            print(i+1,info_Specializations[i].get_text())


        
        
        

