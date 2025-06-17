#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


#Receba os valores do usuario
print("Digite dois numeros e escolha se quer multiplicar e dividir ou somar e subtrair")
nota_01 = float(input("Digite o primeiro número: "))
nota_02 = float(input("Digite o segundo número: "))
print("Digite 1 para multiplicar e dividir")
print("Digite 2 para somar e subtrair")
print("Digite 3 para fazer ambas")
valor = float(input("Digite o valor: "))
if valor == 1:
    multiplicacao = nota_01 * nota_02
    divisao = nota_01 / nota_02
    print(nota_01,"x", nota_02, ":", multiplicacao)
    print(nota_01, "/", nota_02, ":", divisao)
elif valor == 2:
    soma = nota_01 + nota_02
    subtracao = nota_01 - nota_02
    print(nota_01, "+", nota_02, ":", soma)
    print(nota_01, "-", nota_02, ":", subtracao,)
elif valor == 3:
    multiplicacao = nota_01 * nota_02
    divisao = nota_01 / nota_02
    print(nota_01,"x", nota_02, ":", multiplicacao)
    print(nota_01, "/", nota_02, ":", divisao)
    soma = nota_01 + nota_02
    subtracao = nota_01 - nota_02
    print(nota_01, "+", nota_02, ":", soma)
    print(nota_01, "-", nota_02, ":", subtracao)
elif valor != 1 and valor != 2 and valor != 3:
  print("Opção inválida. Por favor, digite 1, 2 ou 3.")

