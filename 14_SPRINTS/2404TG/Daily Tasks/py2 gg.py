# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VASUTcbeQJp3HK9WH4FSKWYq5wm36Jc9
"""

placar_time1 = int(input("Digite o placar do time"))
placar_time2 = int(input("Digite o placar do time"))

if placar_time1 > placar_time2:
  print("Vitoria time 1")
elif placar_time2 > placar_time1:
  print("Vitoria time 2")
else:
  print("Empate")