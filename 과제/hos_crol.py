import requests
from bs4 import BeautifulSoup


class Doctor:
    name = None
    major = None
    specialization = None
    def __init__(self, name, major, Specialization) -> None:
        self.name = name
        self.major=major
        self.specialization=Specialization






if __name__== "__main__":
    response=requests.get("https://www.inha.com/page/department/medicine/doctor")

    if response.status_code!=200:
        print("fail to get data")
    else:
        html=response.text
        soup=BeautifulSoup(html,'lxml')
        ul=soup.select_one("#doctorForm > div.contents > ul")
        majors=ul.select("li > a > p.dept > span")
        info_names=ul.select("li > a > p.name")
        info_Specializations=ul.select(" li > a > p.text01")  
        #doctorForm > div.contents > ul > li:nth-child(1) > a > p.text01
        
        doctors = []        
        for i in range(len(majors)):
            major = majors[i].get_text()
            name = info_names[i].get_text()
            specialization = info_Specializations[i].get_text()
            d = Doctor(name,major,specialization)
            doctors.append(d)

        for i in range(len(doctors)):
            print(i+1, " doctor info")
            print("\tname:", doctors[i].name)
            print("\tmajor:", doctors[i].major)
            print("\tspecialization:", doctors[i].specialization)






        
        
        

