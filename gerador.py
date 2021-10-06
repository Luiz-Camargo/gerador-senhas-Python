import random
import PySimpleGUI as sg #FAZER TELAS
import time

# GERADOR DE SENHAS

minusculo = ("abcdefghjklmnopqrstuvwxyz")
maiusculo = ("ABCDEFGHJKLMNOPQRSTUVWXYZ")
numeros = ("0123456789")
simbolos = ("@#$%&*")

varjuntas = minusculo + maiusculo + numeros + simbolos
tamanho = input("Insira o tamanho da senha:")
nmrsenhas = input("Informe o número de senhas que deve ser gerada:")

for senha in range(int(nmrsenhas)):
    senha = random.sample(varjuntas, int(tamanho))
    print("".join(senha))

    time.sleep(1)