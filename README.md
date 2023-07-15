# College Towns Data ETL | Data Engineering Project
This project focuses on ranking the best college towns for remote workers. By leveraging AWS services(S3, EC2,RDS and Quicksight), utilising ETL (Extract, Transform, Load) using Mage-AI data pipeline, we integrate and analyze data from various sources to provide valuable insights. The goal is to empower remote workers in selecting the most suitable college towns based on criteria such as internet speed, median income, coworking spaces, cost of living, and active mobility.

### Architecture:
![architecure](https://github.com/vaadewoyin/College-Towns-Data-ETL-AWS-Mage-Pipeline/blob/main/architecture.png)

### Data sources
<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <table>
    <tr>
      <th>Data Source</th>
      <th>Data obtained (for college towns)</th>
    </tr>
    <tr>
      <td><a href="https://en.wikipedia.org/wiki/List_of_college_towns#United_States">Wikipedia</a></td>
      <td>US College Towns Names</td>
    </tr>
    <tr>
      <td><a href="https://www.speedtest.net/performance/united-states">Speedtest</a></td>
      <td>Internet Speed</td>
    </tr>
    <tr>
      <td><a href="https://www.bestplaces.net">Bestplaces</a></td>
      <td>Demographic Data (Population, Median Age, Median Income, etc.)</td>
    </tr>
    <tr>
      <td><a href="https://www.walkscore.com/">Walkscore</a></td>
      <td>Walkscore and Bikescore</td>
    </tr>
    <tr>
      <td><a href="https://www.cityfeet.com/cont/coworking-space">CityFeet</a></td>
      <td>Number of Coworking Spaces</td>
    </tr>
  </table>
</body>
</html>

### Data stack/Tools used
- Python 

- BeautifulSoup & Selenium framework for webscraping

- Mage-ai for data pipeline

- Aws services: EC2 for VM,S3 buckets for storing raw data, Postgresql on RDS for storing transformed data, Quicksight for visualization.

## Data Integration and Workflow:
Data was collected from various sources, such as Wikipedia, Speedtest, Bestplaces, Walkscore, and CityFeet, using Python with BeautifulSoup and Selenium frameworks for web scraping. The collected data is stored in AWS S3 buckets. Mage-AI data pipeline was used for ETL, the data was cleaned and prepared during transformation phase before loading,ensuring data integrity and consistency. The transformed data is then loaded into a PostgreSQL database on AWS RDS, enabling efficient storage and retrieval. 

## Key Insights From Analysis
After loading the data to postgresql database, the following insights were obtained from the analysis done in the database:
- The college town with the highest number of coworking spaces is Austin, Texas, with 31 coworking spaces.
- There are 73 college towns with a median income above the national average of $70,785.
- Some college towns with high median incomes include Claremont, California ($89,648), Wellesley, Massachusetts ($159,615), Princeton, New Jersey ($116,875), and Aurora, New York ($72,787).
- The average cost of living index for college towns with populations between 50,000 and 100,000 is 101.66.
- Montreat, North Carolina has the highest number of eateries per capita among college towns, with a ratio of 0.87 eateries per person. Other towns with high ratios include Misenheimer, North Carolina (0.42), and Due West, South Carolina (0.38).
- The average download speed in college towns is approximately 202.84 Mbps, while the average upload speed is around 29.73 Mbps.
- There is a moderate positive correlation (correlation coefficient of 0.60) between the median income and the cost of living index in college towns. This suggests that as the median income increases, the cost of living tends to increase as well.
- Here's a table for the top 5 most affordable college towns based on the cost of living index:

|   College Towns     | Cost of Living Index | Rank |
|-------------------|---------------------|------|
| Itta Bena, Mississippi   |        65.3                 |   1    |
| Marion, Indiana              |        66.1                 |   2    |
| Youngstown, Ohio          |        66.1                 |   2    |
| Pittsburg, Kansas           |        66.5                 |   4    |
| Portales, New Mexico    |        68.0                 |   5    |

### Data Model
![ER diagram](https://github.com/vaadewoyin/College-Towns-Data-ETL-AWS-Mage-Pipeline/blob/main/College_Towns_DB_ER_Diagram.png)

### Ranking Method
Ranking Methodology:
To rank the best college towns for remote workers, we employ a weighted sum model. We assign appropriate weights to each criterion , based on the perceived importance of these criteria to remote workers.Factors such as the number of coworking spaces per capita, unemployment rate, active mobility score, and more are carefully evaluated and assigned weights accordingly.This approach ensures that the model reflects the relative significance of each criterion, allowing for a more accurate and informed decision-making process when selecting a college town for remote work.

### Tableau Dashboard
The interactive dashboard below can be accessed @ [my-tableau-profile](https://public.tableau.com/views/collegetownsdashboard/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

<div class='tableauPlaceholder' id='viz1689370845761' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;collegetownsdashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='collegetownsdashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;co&#47;collegetownsdashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
