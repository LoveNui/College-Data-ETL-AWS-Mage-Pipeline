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
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

#load dataframe containing towns to get needed towns name
towns=pd.read_csv('./Downloads/The Best College Towns for Remote Workers Project/us_college_towns_mod.csv')

#format of (town,abbrevation) to input in website's search box
towns=towns.apply(lambda row: row['town'] + ', ' + row['state_abv'], axis=1)
towns=towns.to_list()

def modify_town(town):
    #function takes string(town) and modifies it to suitable format to place in url
    new_text=''
    for i in town.lower().split(','):
        new_text=new_text+i
    town_string=new_text.replace(' ','-')
    return town_string

town_spaces=[]
for town in towns[158:]:
    try:
        #modify town
        town_string=modify_town(town)
        #url
        url=f'https://www.cityfeet.com/cont/{town_string}' + '/coworking-space'
        #go to page
        driver.get(url)
        #get number of coworking space
        town_name=town
        listing=driver.find_element(By.CLASS_NAME, "list-container")
        num_coworking_space=len(listing.find_elements(By.TAG_NAME,'a'))
        town_dict={'town_name':town_name,'num_coworking_space':num_coworking_space}
        
    except:
        continue
    else:
        town_spaces.append(town_dict)
        
print('scraping done')

#save data
df=pd.DataFrame(town_spaces)
df.to_csv('./city_feet_coworking_space_.csv')
