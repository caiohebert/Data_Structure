def merge(self, inicio, meio, fim):
  i1 = inicio
  i2 = meio + 1
  lista = []
  while i1 <= meio and i2 <= fim:   # era p ser &&?
    if v[i1] < v[i2]:             ## compara os dois blocos e vai adicionando na lista
      lista.append(v[i1])
      i1 += 1
   
    if v[i1] > v[i2]:
      lista.append(v[i2])
      i2 += 1
  
  while i1 <= meio:               ## se sobrou elementos, add na lista
    lista.append(v[i1])
    i1 += 1
  
  while i2 <= fim:
    lista.append(v[i2])
    i2 += 1
  
  return lista


def MergeSort(self, inicio, fim):
  meio = (inicio + fim)//2
  if inicio >= fim:
    return fim
    
  if inicio != fim:
    MergeSort(inicio, meio)        ## particiona o vetor em 2 blocos
    MergeSort(meio + 1, fim)
    
    return merge(self, inicio, meio, fim)