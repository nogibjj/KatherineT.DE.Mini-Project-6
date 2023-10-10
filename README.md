# Data Engineering Mini Project 6

## Purpose
This project is aimed to create an ETL-Query pipeline with an external cloud database. Databricks is used here. Then we used the dataset extracted from FiveThrityEight's public datasets to perform extracting, transforming and complex query. 

## Preparation
1. Create codespace
2. Store Databricks' secrets to connect to Databricks

## Steps
1. In my.lib, create three files that perform several functions. Extract.py extract a dataset from a URL. Transform.py cleans and fliters the dataset. Query.py retrieves from the data.
2. Create a main.py script to run each step.
3. Use test_main.py to test each file and step.
4. Save the process in the log file.

## Complex Query
The query retrieves data from births table and groups by month, returns each month's total births and sort by month. 

```
SELECT month, SUM(births)
            FROM default.births2000DB
            GROUP BY month
            ORDER BY month
```
## Check format and test
Use make test command to test the code

<img width="1077" alt="Screen Shot 2023-10-09 at 6 36 04 PM" src="https://github.com/nogibjj/KatherineT.DE.Mini-Project-6/assets/143833511/c5c9db82-9cd3-4c15-8b80-eef743fa6f2a">


Use make lint and format command to check the format

<img width="739" alt="Screen Shot 2023-10-09 at 6 36 18 PM" src="https://github.com/nogibjj/KatherineT.DE.Mini-Project-6/assets/143833511/f6e8dabf-29b2-4b17-aaca-4e8243e1af0d">







