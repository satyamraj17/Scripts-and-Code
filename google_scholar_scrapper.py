# This script scraps the H-Index, number of citations and i10_index of professors when provided with a CSV file and stores the outcome in a CSV file.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import pandas as pd
from time import sleep

data_base = pd.read_csv("prof_list.csv")
prof_name = data_base['Prof_Name']
college = data_base['College']
citations = []
h_index = []
i10_index = []

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.co.in")
google_scholar = " google scholar"

for i in range(len(prof_name)):
    search = driver.find_element(By.XPATH, "//textarea[@type='search']")
    search.clear()
    search_input = prof_name[i] + " " + college[i] + google_scholar
    search.send_keys(search_input)
    search.send_keys(Keys.ENTER)
    prof_page = driver.find_elements(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")[0]
    prof_page.click()
    sleep(2) # type: ignore
    info = driver.find_elements(By.XPATH, "//td[@class='gsc_rsb_std']")
    citations.append(info[0].text)
    h_index.append(info[2].text)
    i10_index.append(info[4].text)
    driver.back()
    sleep(3)

data_base['Citations'] = citations
data_base['h Index'] = h_index
data_base['i10 Index'] = i10_index

data_base.to_csv("Updated_prof_list.csv", index=False)
