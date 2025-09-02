import matplotlib.pyplot as plt # importa o matplotlib.pyplot e abrevia para plt
import pandas as pd # importa o pandas e abrevia para pd
import seaborn as sns # importa o seaborn e abrevia para sns
from pandas.plotting import register_matplotlib_converters # importa o register_matplotlib_converters do pandas.plotting
register_matplotlib_converters() # registra os conversores de datas do matplotlib

# Exercício 4.1
# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('exercicio4/fcc-forum-pageviews.csv') # le o arquivo que vai ser utilizado no exercício
df.set_index('date', inplace=True) # define a coluna date como index (coluna principal)
df.index = pd.to_datetime(df.index) # converte a coluna index (date) para datetime

# Exercício 4.2
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & # filtra os valores que estão acima do quantil 2.5%
    (df['value'] <= df['value'].quantile(0.975)) # filtra os valores que estão abaixo do quantil de 97.5%
]

# Exercício 4.3
# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    
    fig = plt.figure(figsize=(18, 5)) # cria a figura e determina seu tamanho
    plt.plot(df.index, df['value'], color='red', linestyle='-') # cria o gráfico com x sendo a coluna index (date) e y sendo a coluna value, e estiliza a linha do gráfico
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019') # título do gráfico
    plt.xlabel('Date') # nome do eixo x
    plt.ylabel('Page Views') # nome do eixo y

    fig.savefig('line_plot.png') # salva a figura como 'line_plot.png'
    plt.close() # evita duplicar a figura
    return fig # retorna a imagem

# Exercício 4.4
# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot():

    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean().unstack() # agrupa os dados por ana e mês (extraindo da coluna index), o eixo y é a coluna value para ambos os gráficos e também é calculada a média

    fig, ax = plt.subplots(figsize=(10, 8)) # cria a figura e determina seu tamanho
    df_bar.plot(kind='bar', ax=ax) # cria o gráfico e determina o seu tipo
    ax.set_xlabel('Years') # nome do eixo x
    ax.set_ylabel('Average Page Views') # nome do eixo y
    ax.legend( 
        title='Months', # nome da legenda
        labels=[ # nome dos meses para a legenda
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
    )

    fig.savefig('bar_plot.png') # salva a figura como 'bar_plot.png'
    plt.close() # evita duplicar a figura
    return fig # retorna a imagem

# Exercício 4.5
# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). - - Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
def draw_box_plot():

    df_box = df.copy() # copia o dataframe original para uma outra variável
    df_box.reset_index(inplace=True) # reseta o index do dataframa
    df_box['year'] = [d.year for d in df_box.date] # cria uma nova coluna com o ano de cada data
    df_box['month'] = [d.strftime('%b') for d in df_box.date] # cria uma nova coluna com o mês de cada data


    fig, axes = plt.subplots(1, 2, figsize=(22, 6)) # cria a figura e determina seu tamanho

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], palette='deep') # cria o gráfico e determina os valores para os eixos x e y do gráfico a esquerda (axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)') # título do gráfico
    axes[0].set_xlabel('Year') # nome do eixo x
    axes[0].set_ylabel('Page Views') # nome do eixo y

    sns.boxplot(data=df_box, x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1], palette='deep') # cria o gráfico e determina os valores para os eixos x e y do gráfico a direita (axes[1]), além de determinar a ordem dos meses
    axes[1].set_title('Month-wise Box Plot (Seasonality)') # título do gráfico
    axes[1].set_xlabel('Month') # nome do eixo x
    axes[1].set_ylabel('Page Views') # nome do eixo y

    fig.savefig('box_plot.png') # salva a figura como 'box_plot.png'
    plt.close() # evita duplicar a figura
    return fig # retorna a imagem

#para fazer o teste, basta rodar no terminal "python exercicio4/main.py"