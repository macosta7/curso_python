import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('exercicio3/medical_examination.csv')

# 2
height_in_meters = df['height'] / 100
height_square = height_in_meters ** 2
bmi = df['weight'] / height_square
df['overweight'] = np.where(bmi > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']],
                    id_vars=['cardio'], var_name='variable', value_name='value')


    # 6
    df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    df_cat_cardio_0 = df_cat_grouped[df_cat_grouped['cardio'] == 0]
    df_cat_cardio_1 = df_cat_grouped[df_cat_grouped['cardio'] == 1]

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # 7
    sns.barplot(x='variable', y='total', hue='value', data=df_cat_cardio_0, ax=axes[0])
    axes[0].set_title('cardio=0')
    axes[0].set_ylabel('total')

    sns.barplot(x='variable', y='total', hue='value', data=df_cat_cardio_1, ax=axes[1])
    axes[1].set_title('cardio=1')
    axes[1].set_ylabel('total')
    
    # 8
    plt.tight_layout()

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt=".1f",
        center=0, 
        vmax=0.3, 
        ax=ax, 
        square=True,
        linewidths=0.5, 
        cbar_kws={"shrink": .5})

    plt.close(fig)

    # 16
    fig.savefig('heatmap.png')
    return fig
