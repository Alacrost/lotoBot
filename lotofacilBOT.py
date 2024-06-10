import random


pares = ["02", "04", "06", "08", "10", "12",
         "14", "16", "18", "20", "22", "24", ]
impares = ["01", "03", "05", "07", "09", "11",
           "13", "15", "17", "19", "21", "23", "25"]

numeroJogos = int(input("Quantas combinações deseja? "))
quantosPares = int(input("Quantos números pares extrair? "))
quantosImpares = int(input("Quantos números ímpares extrair? "))

for numeroJogos in range(0, numeroJogos):

    jogo = random.sample(pares, quantosPares) + \
        random.sample(impares, quantosImpares)
    jogo.sort()
    print(f" Jogo aleatório {numeroJogos + 1} --> {jogo}")
