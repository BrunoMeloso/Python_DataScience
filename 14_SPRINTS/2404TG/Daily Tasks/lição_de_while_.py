# -*- coding: utf-8 -*-
"""lição de while .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/180OzX5Zxlg-HvlO5zBfOCZGZA7gju2GZ
"""

mas = 0
fem = 0
listaM = []
listaF = []
while True:
    sexo = input("Digite o seu sexo M para masculino e F para feminino , para finalizar degite \"finalizar\": ")

    if sexo == "M":
       mas = mas + 1
       idade_mas = int(input("Digite a idade: "))
       print(f"genero {sexo} e idade {idade_mas}")
       listaM.append(idade_mas)
       print(f"{listaM}")
    elif sexo == "F":
        fem = fem + 1
        idade_fem = int(input("Digite a idade: "))
        print(f"genero {sexo} e idade {idade_fem}")
        listaF.append(idade_fem)
        print(f"{listaF}")
    elif sexo == "finalizar":
        break

clientes = int(input("Digite a quantidade de pessoas: "))

for i in range(clientes):
    temperatura= float(input("Digite a temperatura: "))
    if temperatura >= 37.2:
        print("normal")
    elif temperatura >= 37.9:
        print("febril")
    elif temperatura >= 38.9:
        print("febre")
    else:
        print("febre alta")

media =  temperatura / i
print(f"quantidade de pessoas analisadas {i} \nmedia das temperaturas {media}")

for i in range(5,100):
  if i % 7 == 0:
    if i % 5 != 0:
      print(i)