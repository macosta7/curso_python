# Exercício 2 - FreeCodeCamp - Python
## Demographic Data Analyzer

In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

You must use Pandas to answer the following questions:

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (```race``` column) **(Exercicio 2.1)**
- What is the average age of men? **(Exercicio 2.2)**
- What is the percentage of people who have a Bachelor's degree? **(Exercicio 2.3)**
- What percentage of people with advanced education (```Bachelors```, ```Masters```, or ```Doctorate```) make more than 50K? **(Exercicio 2.4)**
- What percentage of people without advanced education make more than 50K? **(Exercicio 2.5)**
- What is the minimum number of hours a person works per week? **(Exercicio 2.6)**
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K? **(Exercicio 2.7)**
- What country has the highest percentage of people that earn >50K and what is that percentage? **(Exercicio 2.8)**
- Identify the most popular occupation for those who earn >50K in India. **(Exercicio 2.9)**

Use the starter code in the file ```demographic_data_analyzer.py```. Update the code so all variables set to ```None``` are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

Link GitPod: https://gitpod.io#snapshot/7c6f80f4-a706-4b12-8c08-381fec73ba41