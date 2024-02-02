# programa principal

import RadixSort
import sys

# ********************************************************

# abrir o arquivo com as placas a serem ordenadas
arq = open(sys.argv[1])

# ler e criar uma lista de strings com as placas
placas = arq.readlines()

# ordena as placas
placas = RadixSort.RadixSort(placas)

# cria o novo arquivo
arq_novo = open("ordenadas.piv", "w")

# escreve no novo arquivo a lista com as placas ordenadas
for placa in placas:
    arq_novo.write(placa)

print("Arquivo baixado.")