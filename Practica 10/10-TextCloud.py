
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import os

def Open_File(path: str) -> str:
    content = ""
    datos = pd.read_csv(path)
    content = datos['Equipo']
    return " ".join(content)

def Main() -> None:
  all_words = ""
  frase = Open_File("./csv/olimpicos_limpio.csv") 
  palabras = frase.rstrip().split(" ")

  Counter(" ".join(palabras).split()).most_common(10)

  for arg in palabras:
      tokens = arg.split()
      all_words += " ".join(tokens) + " "

  print(all_words)
  wordcloud = WordCloud(background_color="white", min_font_size=5).generate(all_words)

  plt.close()
  plt.figure(figsize=(5, 5), facecolor=None)
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.tight_layout(pad=0)
  plt.savefig("./Word_Cloud.png")
  plt.close()

if __name__ == "__main__":
    Main()
