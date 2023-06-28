#necessary imports
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver_path = '/usr/local/python/3.10.4/lib/python3.10/site-packages/chromedriver_autoinstaller/112/chromedriver'
service = Service(driver_path)

prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.managed_default_content_settings.javascript": 2,
         "profile.managed_default_content_settings.cookies": 2,
         "profile.managed_default_content_settings.plugins": 1,
         "profile.managed_default_content_settings.popups": 2,
         "profile.managed_default_content_settings.geolocation": 2,
         "profile.managed_default_content_settings.media_stream": 2,
         "profile.managed_default_content_settings.notifications": 2}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=service, options=options)

towns=pd.read_csv('./The Best College Towns for Remote Workers Project/us_college_towns_mod.csv')

#format of (town,abbrevation) to input in website's search box
towns=towns.apply(lambda row: row['town'] + ', ' + row['state_abv'], axis=1)
towns=towns.to_list()

#store collected info
town_details=[]
#go to page
url='https://www.bestplaces.net/find/'
driver.get(url)

#searchbox
#input_element=driver.find_element(By.CSS_SELECTOR,'#txtSearch')
for town in towns:
    try:
        #input text to search
        driver.find_element(By.CSS_SELECTOR,'#form1 > nav > ul > li:nth-child(3) > a > svg').click()
        #locate box
        new_input=driver.find_element(By.CSS_SELECTOR,'#mainContent_txtSearch')
        #input new text to search
        ind=(town.index(','))+2
        text_to_input=town[:ind+2]
        new_input.send_keys(text_to_input)
        #search input
        driver.find_element(By.CSS_SELECTOR,'#mainContent_btnGo1').click()
    except:
        continue
    else:
        try:
            #extract details
            name=town.split(',')[0]
            state=town.split(',')[1].strip()
            population=driver.find_element(By.CSS_SELECTOR,'#form1 > div.bt-0.my-0 > div > div > div:nth-child(5) > div:nth-child(1) > p:nth-child(2)').text
            unemployment_rate=driver.find_element(By.CSS_SELECTOR,'#form1 > div.bt-0.my-0 > div > div > div:nth-child(5) > div:nth-child(1) > p:nth-child(5)').text
            median_income=driver.find_element(By.CSS_SELECTOR,'#form1 > div.bt-0.my-0 > div > div > div:nth-child(5) > div:nth-child(2) > p:nth-child(2)').text
            median_age=driver.find_element(By.CSS_SELECTOR,'#form1 > div.bt-0.my-0 > div > div > div:nth-child(5) > div:nth-child(3) > p:nth-child(2)').text
            cost_of_living=driver.find_element(By.CSS_SELECTOR,"#form1 > div.container > div:nth-child(2) > div.col-sm-4.col-md-6.col-lg-6.col-xl-7 > div.row.mt-2.mb-3 > div:nth-child(2)").text.                                    split('\n')[1].split('Cost of Living:')[1].strip()
            #store extracted details in dictionary
            town_dict={}
            town_dict={'state':state,'name':name,'population':population,'unemployment_rate':unemployment_rate,
                            'median_income':median_income,'median_age':median_age,
                            'cost_of_living':cost_of_living}
            town_details.append(town_dict)
        except :
            print('error:')
        
df=pd.DataFrame(town_details)

#save to disk
df.to_csv('./best_places.csv')
