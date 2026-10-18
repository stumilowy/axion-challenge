import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

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

def generate_plot_and_save(data, labels, title):
  df_chart = pd.DataFrame(data, columns=['Wymiar 1', 'Wymiar 2'])
  df_chart['label'] = labels

  fig, ax = plt.subplots(figsize=(12, 8), facecolor='k')
  ax.set_facecolor('k')

  sns.scatterplot(
      x='Wymiar 1',
      y='Wymiar 2',
      hue='label',
      palette='tab10',
      data=df_chart,
      alpha=0.7,
      s=15,
      ax=ax,
  )

  ax.set_title(title, color='white', fontsize=14)
  ax.xaxis.label.set_color('white')
  ax.yaxis.label.set_color('white')
  ax.tick_params(colors='white')

  for spine in ax.spines.values():
    spine.set_color('white')

  legend = plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
  plt.setp(legend.get_texts(), color='white')
  legend.get_frame().set_facecolor('#1c1c1c')
  legend.get_frame().set_edgecolor('white')

  plt.tight_layout()

  images_dir = Path(__file__).parent.parent / 'images'
  images_dir.mkdir(parents=True, exist_ok=True)
  safe_title = title.replace(' ', '-')

  plt.savefig(
      images_dir / f'{safe_title}.png',
      facecolor=fig.get_facecolor(),
      edgecolor='none',
      bbox_inches='tight',
  )
  plt.show()

def get_clothes_mapping():
    return clothes_dict