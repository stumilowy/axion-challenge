import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

clothes_dict = {
    0: 'T-shirt/top',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle boot',
    10: 'Upper long' # Pullover, Coat, Shirt
}

def generate_plot(data, labels, title):
    df_chart = pd.DataFrame(data, columns=['Wymiar 1', 'Wymiar 2'])
    df_chart['label'] = labels

    plt.figure(figsize=(12, 8))

    sns.scatterplot(
        x='Wymiar 1',
        y='Wymiar 2',
        hue='label',
        palette='tab10',
        data=df_chart,
        alpha=0.7,
        s=15
    )

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def get_clothes_mapping():
    return clothes_dict