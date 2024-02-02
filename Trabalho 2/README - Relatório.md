# Relátorio do Problema 02
## Aluno: Caio Hebert Souza Viana
De início, é importante ressaltar que, para fazer as pilhas e filas foi usada como como base a **lista encadeada**, por ser uma estrutura mais maleável e por não precisar que o seu tamanho seja limitado, o que convém para esse problema em que quantidades aleatórias de pacientes e leitos chegam em cada simulação.

Além disso, o gerenciador de leitos foi feito com **9 filas de pacientes**, uma fila para cada gravidade em cada faixa etária, visto que facilita bastante essa triagem e o manuseamento dos pacientes, evitando a necessidade de realizar buscas pelas filas para inserir novos pacientes se as 3 gravidades estivessem em uma única fila.

Em seguida, foram criadas **3 pilhas** para armazenar os leitos das 3 faixas etárias disponíveis. Nesse sentido, a pilha foi escolhida para armazenar os leitos pelos requisitos do próprio problema, nos quais especificamente era dito que os leitos que chegaram mais recentemente deveriam ser os primeiros a serem liberados para uso. Como a política da pilha é a de ***"Ultimo a Entrar, Primeiro a Sair"***, ou em inglês ***"Last In, First Out"***, ela é o TAD perfeito para o caso. 

Sobre os números usados como atributos dos pacientes e leitos:
* A idade deos pacientes está definida no intervalo de 0 a 94 por convenção social da idade humana.

* O número de identificação dos pacientes foi definidido pelo intervalo de 0 a 100000 para representar uma fração do total de baianos cadastrados no SUS, escolhido para não ser nem muito grande nem muito pequeno. O mesmo vale para os leitos.

* sobre os intervalos dos geradores de quantidade de pacientes e leitos, as quantidades de 40 e 30 foram escolhidas para representar, também, uma fração da população e para gerarem quantidades pequenas de demanda que podem ser acumuladas em cada situação/simulação.

Nesse contexto, um outro detalhe importante é o intervalo usado para gerar os tipos de leito de acordo com a faixa etária. Num primeiro momento foi posto apenas os números 1, 2 e 3 para os tipos de leito. Porém, nota-se que isso faria aumentar a quantidade de leitos de neonatal, pois teriam uma probabilidade parecida de serem gerados, enquanto os pacientes nessa idade tem uma probabilidade muito baixa de serem gerados. Logo, foi incrementado o intervalo de números que geram esses tipos para que os leitos de neonatal surjam em menor quantidade, com o intuito de fazer o simulador ser um pouco mais próximo da realidade. 
