import numpy as np #importa o numpy abreviando para np

def calculate(list): #função para calcular os valores pedidos
    if len(list) != 9: #se a lista não tiver 9 elementos:
        raise ValueError("List must contain nine numbers.") #retorna um erro

    matriz = np.array(list).reshape(3,3) #transforma a lista em uma matriz 3x3

    mean_axis0 = matriz.mean(axis=0).tolist() #calcula a média dos valores da matriz por linha
    mean_axis1 = matriz.mean(axis=1).tolist() #calcula a média dos valores da matriz por coluna
    mean_flattened = matriz.mean().tolist() #calcula a média dos valores da matriz

    var_axis0 = matriz.var(axis=0).tolist() #calcula a variância dos valores da matriz por linha
    var_axis1 = matriz.var(axis=1).tolist() #calcula a variância dos valores da matriz por coluna
    var_flattened = matriz.var().tolist() #calcula a variância dos valores da matriz

    std_axis0 = matriz.std(axis=0).tolist() #calcula o desvio padrão dos valores da matriz por linha
    std_axis1 = matriz.std(axis=1).tolist() #calcula o desvio padrão dos valores da matriz por coluna
    std_flattened = matriz.std().tolist()   #calcula o desvio padrão dos valores da matriz

    max_axis0 = matriz.max(axis=0).tolist() #calcula o valor máximo dos valores da matriz por linha
    max_axis1 = matriz.max(axis=1).tolist() #calcula o valor máximo dos valores da matriz por coluna
    max_flattened = matriz.max().tolist() #calcula o valor máximo dos valores da matriz

    min_axis0 = matriz.min(axis=0).tolist() #calcula o valor mínimo dos valores da matriz por linha
    min_axis1 = matriz.min(axis=1).tolist() #calcula o valor mínimo dos valores da matriz por coluna
    min_flattened = matriz.min().tolist() #calcula o valor mínimo dos valores da matriz

    sum_axis0 = matriz.sum(axis=0).tolist() #calcula a soma dos valores da matriz por linha
    sum_axis1 = matriz.sum(axis=1).tolist() #calcula a soma dos valores da matriz por coluna
    sum_flattened = matriz.sum().tolist() #calcula a soma dos valores da matriz

    result = { #cria um dicionário com os resultados
        'mean': [mean_axis0, mean_axis1, mean_flattened],
        'variance': [var_axis0, var_axis1, var_flattened],
        'standard deviation': [std_axis0, std_axis1, std_flattened],
        'max': [max_axis0, max_axis1, max_flattened],
        'min': [min_axis0, min_axis1, min_flattened],
        'sum': [sum_axis0, sum_axis1, sum_flattened]
    }

    return result #retorna o dicionário com os resultados

#para fazer o teste, basta rodar no terminal "python exercicio1/main.py"