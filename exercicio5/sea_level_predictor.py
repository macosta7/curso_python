import pandas as pd #importa o pandas e abrevia para pd
import matplotlib.pyplot as plt #importa o matplotlib e abrevia para plt
from scipy.stats import linregress #importa a função linregress do scipy.stats

def draw_plot():
    #Exercício 5.1
    #Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('exercicio5/epa-sea-level.csv') # le o arquivo que vai ser utilizado no exercício

    #Exercício 5.2
    #Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.figure(figsize=(10, 6)) #define o tamanho da figura
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level']) #cria o gráfico de dispersão

    #Exercício 5.3
    #Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level']) #calcula a regressão linear
    x = range(df['Year'].min(), 2051, 1) #cria um vetor de anos de 1880 a 2050
    y = res.slope * x + res.intercept #calcula o valor de y para cada valor de x
    plt.plot(x, y, 'r', label='Ajuste (toda a série)') #plota a reta de regressão linear

    #Exercício 5.4
    #Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_recent = df[df['Year'] >= 2000] #cria um novo dataframe com os dados a partir de 2000
    plt.scatter(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']) #cria o gráfico de dispersão a partir de 2000
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']) #calcula a regressão linear a partir de 2000
    x_recent = range(df_recent['Year'].min(), 2051, 1) #cria um vetor de anos de 2000 a 2050
    y_recent = res_recent.slope * x_recent + res_recent.intercept #calcula o valor de y para cada valor de x a partir de 2000
    plt.plot(x_recent, y_recent, 'g', label='Ajuste (desde 2000)') #plota a reta de regressão linear a partir de 2000

    #Exercício 5.5
    #The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.xlabel("Year") #Nome do eixo x
    plt.ylabel("Sea Level (inches)") #Nome do eixo y
    plt.title("Rise in Sea Level") #Título do gráfico
    plt.legend() #Legenda do gráfico
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

#para fazer o teste, basta rodar no terminal "python exercicio5/main.py"