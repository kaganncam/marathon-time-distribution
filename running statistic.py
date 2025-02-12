import time 
from bs4 import BeautifulSoup
from matplotlib import pyplot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://event.spor.istanbul/eventresults.aspx"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 9.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"}

start_time = time.time()
driver = webdriver.Firefox()
driver.get("https://event.spor.istanbul/eventresults.aspx")
finded_element = driver.find_element(By.ID,"ddlCategory")
Select(finded_element).select_by_value("5ce92839-d70d-4fe1-b504-eb5673682e99")

time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) 
    
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        time.sleep(3)  # 3sn ek
        new_source = driver.page_source
        if new_source == driver.page_source: 
            break

    last_height = new_height
##
source = driver.page_source
data_set = [] 

soup = BeautifulSoup(source,"html.parser")
    
rows = soup.find_all("tr",class_ = "TableResultRow" )
    
for row in rows:
    columns = row.find_all("td")
    data = [col.text.strip() for col in columns ]
    data_set.append(data)
    
file_name = "spor-ist-sonuclar.text"
with open(file_name,"w",encoding = "utf-8") as file:
    for row in data_set:
        file.write(" ".join(row)  + "\n")

end_time = time.time()
execution_time =  end_time - start_time
print(f"{len(data_set)} sayıda öğe yazdırldı")
print(f"Executed in {execution_time:.2f}")