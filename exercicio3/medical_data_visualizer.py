import pandas as pd # importa o pandas abreviado como pd
import seaborn as sns # importa o seaborn abreviado como sns
import matplotlib.pyplot as plt # importa o matplotlib.pyplot abreviado como plt
import numpy as np # importa o numpy abreviado como np

# Exercício 3.1
# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('exercicio3/medical_examination.csv')  # le o arquivo que vai ser utilizado no exercicio

# Exercício 3.2
# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
height_in_meters = df['height'] / 100 # converte a altura de cm para metros
height_square = height_in_meters ** 2 # calcula o quadrado da altura
bmi = df['weight'] / height_square # calcula o bmi (peso / altura²)
df['overweight'] = np.where(bmi > 25, 1, 0) # adiciona a coluna overweight com 1 para acima de 25 e 0 para abaixo de 25

# Exercício 3.3
# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1) # se o valor for 1, muda para 0, se for maior que 1, muda para 1
df['gluc'] = np.where(df['gluc'] == 1, 0, 1) # se o valor for 1, muda para 0, se for maior que 1, muda para 1

# Exercício 3.4
# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # Exercício 3.5
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']], # colunas que serão usadas
                    id_vars=['cardio'], var_name='variable', value_name='value') # coluna que será usada como referência (cardio)

    # Exercício 3.6
    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']) # agrupa os dados por cardio (0 e 1)e mostra a contagem de cada feature

    # Exercício 3.7
    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    fig = sns.catplot(data=df_cat, x='variable', hue='value', kind='count', col='cardio') # cria o gráfico de barras com os dados agrupados por cardio e conta a quantidade de cada feature

    # Exercício 3.8
    # Get the figure for the output and store it in the fig variable.
    fig.set_axis_labels('variable', 'total') # renomeia os eixos x ('variable') e y ('total')

    plt.close(fig.fig) # fecha o gráfico para evitar que o gráfico seja exibido duas vezes

    fig.fig.savefig('catplot.png') # salva o gráfico em um arquivo png
    return fig.fig


# Exercício 3.9
# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Exercício 3.10
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    df_heat = df[ # filtra os dados de acordo com as condições pedidas no exercício
        (df['ap_lo'] <= df['ap_hi']) & # Exercício 3.10.1
        (df['height'] >= df['height'].quantile(0.025)) & # Exercício 3.10.2
        (df['height'] <= df['height'].quantile(0.975)) & # Exercício 3.10.3
        (df['weight'] >= df['weight'].quantile(0.025)) & # Exercício 3.10.4
        (df['weight'] <= df['weight'].quantile(0.975)) # Exercício 3.10.5
    ]

    # Exercício 3.11
    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr() # calcula a matriz de correlação

    # Exercício 3.12
    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool)) # cria uma máscara para a parte superior da matriz de correlação para não repetir os valores

    # Exercício 3.13
    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(11, 9)) # cria a figura com o tamanho desejado

    # Exercício 3.14
    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap( # cria o gráfico de calor
        corr, # dados a serem plotados
        mask=mask, # máscara para a parte superior da matriz de correlação (evitar repetição de valores)
        annot=True, # anotação dos valores
        fmt=".1f", # valores com uma casa decimal
        center=0, # centraliza os valores em 0
        vmax=0.3, # valor máximo do eixo y
        ax=ax, # eixo do gráfico
        square=True, # formato quadrado
        linewidths=0.5, # largura da linha
        cbar_kws={"shrink": .5}) # tamanho da barra de cores

    plt.close(fig) # fecha o gráfico para evitar que o gráfico seja exibido duas vezes

    # 16
    fig.savefig('heatmap.png') # salva o gráfico em um arquivo png
    return fig

#para fazer o teste, basta rodar no terminal "python exercicio3/main.py"