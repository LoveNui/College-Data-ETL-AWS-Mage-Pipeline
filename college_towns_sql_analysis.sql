--Which college town has the highest number of coworking spaces?
SELECT college_towns,num_coworking_space 
FROM coworking_spaces cs 
ORDER BY num_coworking_space  DESC
LIMIT 1;

/*Which college towns have a median income above the national average?
  (The Census Bureau reported that real U.S. median household income in 2021 was $70,785)*/
SELECT COUNT(median_income) AS "No of towns with high median income"
FROM demographics d 
WHERE median_income >70785;

SELECT college_towns,median_income
FROM demographics d 
WHERE median_income >70785;

--What is the average cost of living index for college towns with a populations between 50000-100000?
SELECT AVG(cost_of_living_index) AS "AVG. COST OF LIVING INDEX FOR POP. BETWEEN 50k and 100k"
FROM demographics d 
WHERE population BETWEEN 50000 AND 100000;

--Which college towns have the highest number of eateries per capita?
SELECT d.college_towns, ws.num_eateries, d.population, 
		(CAST(ws.num_eateries AS DECIMAL) / CAST(d.population AS DECIMAL)) AS eateries_per_capita
FROM demographics d
JOIN walkability_scores ws
ON d.college_towns = ws.college_town
ORDER BY eateries_per_capita desc 
LIMIT 10;

--Do college towns with a higher number of coworking spaces tend to have a higher median income?
SELECT d.college_towns, d.median_income, cs.num_coworking_space
FROM demographics d
JOIN coworking_spaces cs ON d.college_towns = cs.college_towns
ORDER BY cs.num_coworking_space DESC
LIMIT 10;

--What is the average internet speed (download and upload) in college towns?
SELECT AVG(median_download_speed),AVG(median_upload_speed)
FROM internet_speed
;

--Is there a correlation between the median income and the cost of living index in college towns
SELECT corr(median_income, cost_of_living_index) AS correlation_coefficient
FROM demographics;

/*Are there any significant differences in the demographic profiles (age, income, etc.) between 
 college towns with a high number of coworking spaces and those with a low number*/
SELECT d.college_towns, d.median_age, d.median_income, cs.num_coworking_space
FROM demographics d
JOIN coworking_spaces cs ON d.college_towns = cs.college_towns
ORDER BY cs.num_coworking_space;

--How does the unemployment rate vary across different age groups in college towns?
WITH age_groups AS (
    SELECT college_towns,
           CASE
               WHEN median_age < 25 THEN 'Under 25'
               WHEN median_age >= 25 AND median_age < 35 THEN '25-34'
               WHEN median_age >= 35 AND median_age < 45 THEN '35-44'
               ELSE '45 and above'
           END AS age_group,
           unemployment_rate
    FROM demographics
)
SELECT age_group, AVG(unemployment_rate) AS average_unemployment_rate
FROM age_groups
GROUP BY age_group;

--Rank of college towns based on their cost of living index, from the most affordable to the most expensive
SELECT college_towns, cost_of_living_index,
	RANK() OVER(ORDER BY cost_of_living_index)
FROM demographics d ;

/*Rank of college towns based on their walkability score and median income, 
 * from the most walkable with the highest median income to the least walkable with the lowest median income.*/
SELECT d.college_towns, ws.walk_score, d.median_income,
           RANK() OVER (ORDER BY ws.walk_score DESC, d.median_income DESC) AS ranking
FROM demographics d
JOIN walkability_scores ws 
ON d.college_towns = ws.college_town;