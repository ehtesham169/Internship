from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import re

driver=webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
website1="https://free-braindumps.com/login.html"
driver.get(website1)
username=driver.find_element_by_id("UserName")
username.clear()
username.send_keys("ehtesham_ali@live.com")
password=driver.find_element_by_id("Password")
password.clear()
password.send_keys("Log23/")
button=driver.find_element_by_id("LoginButton")
button.click()
time.sleep(5)
file = open("Questions.txt", "a")
removal = "\n"
removal2 = ":"
removal3 = ";"
removal4 = ","
removal5 = "()"
removal6 = "<div>"
removal7 = "<br/>"
removal8 = "<br>"
removal9 = "<b>"
removal10 = "</b>"
removal11 = "</div>"
removal12 = "/p"
removal13="<li>"
mydata = ""
for i in range(2,691):
    stringno=str(i)
    website2 = "https://free-braindumps.com/pmi/free-pmp-braindumps.html?p=" + stringno
    driver.get(website2)
    content = driver.page_source
    soup = BeautifulSoup(content,features="lxml")
    for a in soup.findAll('div', attrs={'class':'panel-body'}):
        mydata += str(a)
        mydata = re.sub(removal, "", mydata)
        mydata = re.sub(removal2, "", mydata)
        mydata = re.sub(removal3, "", mydata)
        mydata = re.sub(removal4, "", mydata)
        mydata = re.sub(removal5, "", mydata)
        mydata = re.sub(removal6, "", mydata)
        mydata = re.sub(removal7, "", mydata)
        mydata = re.sub(removal8, "", mydata)
        mydata = re.sub(removal9, "", mydata)
        mydata = re.sub(removal10, "", mydata)
        mydata = re.sub(removal11, "", mydata)
    file.write(mydata)
    print("page no:" + stringno)

print("finished")