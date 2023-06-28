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

us_towns_internet=[]

#get url
url ='https://www.speedtest.net/performance/united-states'
driver.get(url)

#get states tags
states=driver.find_element(By.CLASS_NAME,"performance-place-listing").find_elements(By.TAG_NAME,'a')
state_links=[]
#get all state link
for state in states:
    state_links.append(state.get_attribute('href'))
    
for state_link in state_links:   
    #open new tab
    driver.execute_script("window.open('');")
    # Switch to the new window and open new state url
    driver.switch_to.window(driver.window_handles[1])
    driver.get(state_link)

    towns=driver.find_element(By.CLASS_NAME,"performance-place-listing").find_elements(By.TAG_NAME,'a')
    town_links=[]
    #get all town link
    for town in towns:
        town_links.append(town.get_attribute('href'))

    for town_link in town_links:    
        #open new tab
        try:
            driver.execute_script("window.open('');")
            # Switch to the new window and open new state url
            driver.switch_to.window(driver.window_handles[2])
            driver.get(town_link)

            state_name=driver.title.split('United States')[0].split(',')[1].strip()
            town_name=driver.title.split('United States')[0].split(',')[0]
            median_download_speed=driver.find_element(By.ID,"fixed").text.split('\n')[2]
            median_upload_speed=driver.find_element(By.ID,"fixed").text.split('\n')[5]
            median_latency=driver.find_element(By.ID,"fixed").text.split('\n')[8]
        except:
            try:
                driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/main/div[2]/div/div/div/div/a[2]').click()
                wait = WebDriverWait(driver, 1)
                median_download_speed= wait.until(EC.presence_of_element_located((By.ID,"fixed"))).text.split('\n')[2]
                median_upload_speed=driver.find_element(By.ID,"fixed").text.split('\n')[5]
                median_latency=driver.find_element(By.ID,"fixed").text.split('\n')[8]
                town_dict={}
                town_dict={'state_name':state_name,'town_name':town_name,'median_download_speed':median_download_speed,
                          'median_upload_speed':median_upload_speed,'median_latency':median_latency}
                us_towns_internet.append(town_dict)
                driver.close()
                driver.switch_to.window(driver.window_handles[1])
            except:
                driver.close()
                driver.switch_to.window(driver.window_handles[1])
                continue    
        else:
            town_dict={}
            town_dict={'state_name':state_name,'town_name':town_name,'median_download_speed':median_download_speed,
                          'median_upload_speed':median_upload_speed,'median_latency':median_latency}
            us_towns_internet.append(town_dict)

            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            
print('scraping done')

df=pd.DataFrame(us_towns_internet)

#save to disk
df.to_csv('./us_towns_internet_full.csv')

