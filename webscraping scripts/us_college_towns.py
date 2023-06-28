#necessary imports
import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

#get url
url='https://en.wikipedia.org/wiki/List_of_college_towns#United_States'
html=requests.get(url)
html_text=html.text

#parse html_text
soup=BeautifulSoup(html_text,'lxml')

#get list of US college towns
us_college_towns=[]

#li_tags to get needed colleges
li_tags=soup.find_all('li')
#get index of needed colleges
for element in li_tags:
    try: 
        if element.a.get('title')=='Auburn, Alabama':
            first_index=li_tags.index(element)
            print('first_index :',li_tags.index(element))
        if element.a.get('title')=='Laramie, Wyoming':
            second_index=li_tags.index(element)
            print('second_index :',li_tags.index(element))
    except:
        continue

#extract colleges within specified range
for element in range(first_index,(second_index+1)):
    us_college_towns.append((li_tags[element]).a.get('title'))
print('Number of US college towns scrapped :',len(us_college_towns))

#save extracted us college town names
us_college_towns_df=pd.DataFrame(us_college_towns,columns=['US college towns'])
us_college_towns_df.to_csv('./us_college_towns.csv',index=False)

