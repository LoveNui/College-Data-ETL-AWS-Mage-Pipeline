#Necessary imports
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.managed_default_content_settings.javascript": 2,
         "profile.managed_default_content_settings.cookies": 2,
         "profile.managed_default_content_settings.plugins": 2,
         "profile.managed_default_content_settings.popups": 2,
         "profile.managed_default_content_settings.geolocation": 2,
         "profile.managed_default_content_settings.media_stream": 2,
         "profile.managed_default_content_settings.notifications": 2}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('prefs', prefs)

# Define Chrome options
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # run Chrome in headless mode
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()

#timeout for loadtime as 5 secs
driver.set_page_load_timeout(5)

#load data containing towns name
towns=pd.read_csv('./us_college_towns_mod.csv')

#format of (town,abbrevation) to input in website's search box
towns=towns.apply(lambda row: row['town'] + ', ' + row['state_abv'], axis=1)
towns=towns.to_list()

#store collected info
town_details=[]

#get each towns info
for town in towns:
    split_town=town.split(',')
    abv=split_town[1].strip()
    town_string=(split_town[0].strip()).replace(' ','_')
    url_format=f'https://www.walkscore.com/{abv}/'+town_string
    try:
        driver.get(url_format)
        time.sleep(3)
        wait = WebDriverWait(driver, 2)
        scores_box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#hood-badges > div > div > div > div > div')))
        scores=scores_box.find_elements(By.TAG_NAME,'img')
        for score in scores:
            if 'walk'in ((score.get_attribute('alt')).lower()):
                walk_score=score.get_attribute('alt').split(' ')[0]
            elif 'bike' in ((score.get_attribute('alt')).lower()):
                bike_score=score.get_attribute('alt').split(' ')[0]
            else:
                continue
    except:
        #if town has no bike or walk score, skip to next town in loop
        continue
    else:
        try:
            #get number of eateries
            num_eateries=driver.find_element(By.CSS_SELECTOR,'#eat-drink > div > div > div:nth-child(1) > div > div > div > p:nth-child(1)').text.split(' ')[3]
        except:
            #if num_eateries missing, assign 0 and complete sequence of code
            num_eateries=0
            town_name=town.split(',')[0]
            town_dict={}
            town_dict={'town_name':town_name,'walk_score':walk_score,'bike_score':bike_score,
                            'num_eateries':num_eateries} #store extracted details in dictionary
            town_details.append(town_dict)
        else:
            #if no exception raised:
            #store extracted details in dictionary
            town_name=town
            town_dict={}
            town_dict={'town_name':town_name,'walk_score':walk_score,'bike_score':bike_score,
                            'num_eateries':num_eateries} #store extracted details in dictionary
            town_details.append(town_dict)

df=pd.DataFrame(town_details)

#save to disk
df.to_csv('./walk_score_final.csv')

