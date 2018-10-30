## H1B_visa_project

# Problem

```
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.
```

# Approach

```
* I decided to use Python for this project because it's a very powerful data language, and I've coded in python for similar projects in the past

1) Carefully read through the instructions and the "Record Layout" to determine scope and relevant variables
2) Iterate through the csv, and append each line to create a list of dictionaries
3) Use Counter to determine most common (10) values of the "SOC_NAME", and the "WORKSITE_STATE" to determine the top 10 most common Occupations, and Workplace States
4) Using the top 10 Occupations and States as veriables, make a dictionary that iterates through the original dictionary and indexes by those specific ocupations and states and counts the number of the certified visas.
5) divide that number by the total count of certified visas in general reguardless of state and occupation status and record that as a percentage
6) zip the output field names and values together, and have the output be ordered by highest value of "NUMBER_CERTIFIED_APPLICATIONS". In case of tie, order the tied entries by alphabetical order on the values of "TOP_OCCUPATIONS" and "TOP_STATES"
7) Write out the list of dictionaries as a txt file.
8) run the run.sh file
9) run the run_tests.sh file in the test_suites folder
10) Create 2nd test

```


# Run Instructions

```
* I used no external Python libraries, so there is no need to run pip install to run this program
	* The libraries I did use were: csv, Counter and sys

* Clone the repository and add it to Desktop
* Open the filepath in gitbash
* Run the "run.sh" file
* Open the files in the output folder to check answers

* to test: navigate to the "insight_testsuite" folder on gitbash
* run "run_tests.sh" on gitbash
```


