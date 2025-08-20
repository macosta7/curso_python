import pandas as pd #importa o pandas abreviando para pd

def calculate_demographic_data(print_data=True): #funçao para calcular os dados pedidos
    df = pd.read_csv('exercicio2/adult.data.csv') #le o arquivo que vai ser utilizado no exercicio

    #Exercicio 2.1
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts() #conta a quantidade de cada raça e exibe o nome da raça com a quantidade

    #Exercicio 2.2
    # What is the average age of men?
    average_age_men = df.loc[df.sex == "Male", "age"].mean().round(1) #filtra o sexo masculino e calcula a média da idade arredondando para 1 casa decimal, round()

    #Exercicio 2.3
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.loc[df.education == "Bachelors"] #filtra os que tem o ensino de "Bachelors"
    percentage_bachelors = round((percentage_bachelors.shape[0] * 100 / df.shape[0]), 1) #calcula a porcentagem arredondando para 1 casa decimal, round()

    #Exercicio 2.4
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    #Exercicio 2.5
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[((df.education == "Bachelors") | (df.education == "Masters") | (df.education == "Doctorate"))] #filtra os que tem o ensino de "Bachelors", "Masters" ou "Doctorate"
    lower_education = df.loc[~((df.education == "Bachelors") | (df.education == "Masters") | (df.education== "Doctorate"))] #filtra os que não tem o ensino de "Bachelors", "Masters" ou "Doctorate"

    # percentage with salary >50K and with advanced education (exercício 2.4)
    higher_education_rich = df.loc[((df.education == "Bachelors") | (df.education == "Masters") | (df.education == "Doctorate")) & (df.salary == ">50K")] #filtra os que tem o ensino de "Bachelors", "Masters" ou "Doctorate" e ganham mais de 50K
    higher_education_rich = round((higher_education_rich.shape[0] * 100 / higher_education.shape[0]), 1) #calcula a porcentagem arredondando para 1 casa decimal, round()

    # percentage with salary >50K and without advanced education (exercício 2.5)
    lower_education_rich = df.loc[~((df.education == "Bachelors") | (df.education == "Masters") | (df.education == "Doctorate")) & (df.salary == ">50K")] #filtra os que não tem o ensino de "Bachelors", "Masters" ou "Doctorate" e ganham mais de 50K
    lower_education_rich = round((lower_education_rich.shape[0] * 100 / lower_education.shape[0]), 1) #calcula a porcentagem arredondando para 1 casa decimal, round()

    #Exercicio 2.6
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min() #filtra a menor quantidade de horas trabalhadas por semana

    #Exercicio 2.7
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df["hours-per-week"].min() #filtra a menor quantidade de horas trabalhadas por semana
    rich_percentage = df.loc[(df["hours-per-week"] == num_min_workers) & (df.salary == ">50K")] #filtra as pessoas que trabalham a menor quantidade de horas e ganham mais de 50K
    total_num_min_workers = df.loc[df["hours-per-week"] == num_min_workers] #filtra as pessoas que trabalham a menor quantidade de horas
    rich_percentage = round((rich_percentage.shape[0] * 100 / total_num_min_workers.shape[0]), 1) #calcula a porcentagem arredondando para 1 casa decimal, round()

    #Exercicio 2.8
    # What country has the highest percentage of people that earn >50K?
    rich_people = df[df['salary'] == ">50K"] #filtra as pessoas que ganham mais de 50K

    total_people_by_country = df.groupby('native-country').size() #total de pessoas por país, agrupada por país e conta o número de linhas, size()
    rich_people_by_country = rich_people.groupby('native-country').size() #total de pessoas que ganham mais de 50K por país, agrupada por país e conta o número de linhas, size()

    percentage_by_country = (rich_people_by_country / total_people_by_country) * 100 #calcula a porcentagem de pessoas que ganham mais de 50K por país

    highest_earning_country = percentage_by_country.idxmax() #nome do país com a maior porcentagem
    highest_earning_country_percentage = round(percentage_by_country.max(), 1) #porcentagem do país com a maior porcentagem arredondando para 1 casa decimal, round()

    #Exercicio 2.9
    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df[(df['salary'] == ">50K") & (df['native-country'] == "India")] #filtra as pessoas que ganham mais de 50K e que são da "India"
    top_IN_occupation = rich_india['occupation'].value_counts().idxmax() #filtra a ocupação mais popular

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

#para fazer o teste, basta rodar no terminal "python exercicio2/main.py"
