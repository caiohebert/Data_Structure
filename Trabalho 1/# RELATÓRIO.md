# RELATÓRIO

O algoritmo escolhido para essa atividade foi o Radix Sort com base no Counting Sort. Nesse contexto, como é um algoritmo que ordena processando os dígitos das chaves separadamente, é mais eficiente para um problema que necessita de uma ordem lexicográfica para sua resolução. Além disso, como a quantidade de dígitos é fixa para todas as chaves da entrada, é possível obter uma complexidade menor que n*log(n), como está descrito a seguir.

De início, é possível observar que o Counting Sort tem em sua implementação 4 loops principais. O primeiro percorre o vetor *v* (tamanho *n*), o segundo percorre o vetor *conta* (tamanho 91), o terceiro percorre novamente o vetor *v* (tamanho *n*) e o quarto percorre o vetor *saída* (de tamanho *n*, assim como *v*). Assim, temos: O(3n+91), porém, aplicando as diretrizes para análise assintótica, tem-se: O(n+91). 

Em seguida, como o Counting Sort é realizado 7 vezes (referente a quantidade de dígitos das placas) no Radix Sort, a complexidade seria O(7(n+k)), no entanto, como 7 é uma constante, a complexidade final do algoritmo é O(n+91). Dito isso, nota-se que a complexidade obtida é menor que n*log(n) e, assim, o objetivo da atividade foi alcançado.

## Referências Bibliográficas: 
[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012..
