# College Towns Data ETL | Data Engineering Project
The goal of this project is to make a data integration and analysis project focused on college towns. It utilizes AWS services, including S3, EC2,RDS and Quicksight, along with the Mage data pipeline tool for ETL operations.

### Architecture:
![architecure](https://github.com/vaadewoyin/College-Towns-Data-ETL-AWS-Mage-Pipeline/blob/main/architecture.png)

### Data sources
The data used was collected from different sources;

The list of college towns was gotten from [wikipedia](https://en.wikipedia.org/wiki/List_of_college_towns#United_States),

The internet speed was obtained from [Speedtest](https://www.speedtest.net/performance/united-states)

Some demographic data (population,median age, median income etc.) was obtained from [Bestplaces](https://www.bestplaces.net)

Walkscore and Bikescore of each town was obtained from [Walkscore](https://www.walkscore.com/)

Number of coworking space in each town was obtained from [CityFeet](https://www.cityfeet.com/cont/coworking-space)

### Data stack/Tools used
Python 

BeautifulSoup & Selenium framework for webscraping

Mage-ai for data pipeline

Aws services: EC2 for VM,S3 buckets for storing raw data, Postgresql on RDS for storing transformed data, Quicksight for visualization.


### Data Model
![ER diagram](https://github.com/vaadewoyin/College-Towns-Data-ETL-AWS-Mage-Pipeline/blob/main/College_Towns_DB_ER_Diagram.png)

### Pipeline/Workflow
1. The scraped data is stored in s3 bucket
2. Using Mage, data is retrieved from s3 buckets, transformed and loaded to postgresql database on Aws RDs.
3. Using Quicksight, we make visualization using transformed data.

### Tableau Dashboard
The interactive dashboard below can be accessed @ [my-tableau-profile](https://public.tableau.com/views/collegetownsdashboard/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

<div class='tableauPlaceholder' id='viz1689370845761' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;collegetownsdashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='collegetownsdashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;collegetownsdashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
