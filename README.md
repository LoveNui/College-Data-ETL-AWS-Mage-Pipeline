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

### Dashboard
![dashboard](https://github.com/vaadewoyin/College-Towns-Data-ETL-AWS-Mage-Pipeline/blob/main/aws_quicksight_dashboard.png)

