# FUNÇÕES CRIADAS PARA O CÓDIGO

# ***************************************************
def CountingSort(v, indice_str):
    tam = len(v)
    conta = [0] * 91                            # ---> vetor que abarca até o ultimo valor ASCII do alfabeto maiúsculo nos índices
    saida = [0] * tam

    # add +1 onde o valor do char é o indice da lista conta
    for i in range (tam):     
        indice = ord(v[i][indice_str])          # ---> valor em ASCII do char indicado por indice_str na string que será usado como indice na lista "conta"
        conta[indice] += 1

    # soma o numero com seu antecessor
    for j in range (1, 91):       
        conta[j] += conta[j-1]

    # coloca as strings de entrada ordenadas na saida utilizando os indices
    for k in range (tam-1, -1, -1):
        indice = ord(v[k][indice_str])
        saida[conta[indice] - 1] = v[k]      
        conta[indice] -= 1                    
    
    # substitui os valores da saída no vetor original
    for i in range (tam):
        v[i] = saida[i]
    
    return v

# ***************************************************
def RadixSort(v):
    indice_str = 6

    # realiza o counting sort para cada um dos 7 caracteres das strings das placas
    while indice_str >= 0:                
        CountingSort(v, indice_str)
        indice_str -= 1

    return v



