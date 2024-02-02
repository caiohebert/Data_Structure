v = [3, 8, 90, 68, 36]

def QuickSort(v, esq, dir, p):
  if esq != dir:
    for i in range (esq, dir):                  # esq procura elem > p, dir procura menor
      if v[i] > v[p]:
        for j in range (dir, esq, -1):
          if v[j] < v[p]:
            v[i], v[j] = v[j], v[i]
            break        
          if esq > dir:
            v[p], v[j] = v[j], v[p]
            quebra = dir
            break
      if esq > dir:
        break

  QuickSort(esq, quebra, esq)
  QuickSort(quebra + 1, dir, quebra + 1)

  return v
  


def part(esq, p):
  pivo = v[p]
  i = esq

  