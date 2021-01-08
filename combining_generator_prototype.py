# autor: Tiago Ferreira Bonomo
#Protótipo de gerador de combinacções
import math
import random

# dezenas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
dezenas = [1, 2, 3, 4, 5]
combinacoes = []
combinacao = []

c = len(dezenas)
p = 3
n = c - p

fc = math.factorial(c)
fp = math.factorial(p)
fn = math.factorial(n)
res = fc / (fp * fn)
print("Resposta: ", res)

cont_combs = 0
counter_inters = 0
counter_combs = 0

# Combinações a Gerar
while (res > cont_combs):
    combination = random.sample(dezenas, p)
    if len(combinacoes) == 0:
        print("Combination: ", combination)
        combinacoes.append(combination)
        cont_combs = cont_combs + 1

    if len(combinacoes) > 0:

        cont_inters = 0
        for i in combinacoes:
            inters = set(i).intersection(combination)

            if len(inters) == p:
                cont_inters = cont_inters + 1

        if cont_inters == 0:
            print("Combinação: ", combination)
            print("Interceção: ", inters)
            print("Quantidade de Interceções: ", len(inters))
            combinacoes.append(combination)
            cont_combs = cont_combs + 1

for i in combinacoes:
    print("Lista Combinações: ", i)
