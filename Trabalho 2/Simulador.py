import Classes
import random



# ============= SIMULADOR =============

print("_______________________________\n")
print("Bem vindo ao simulador! Vamos inciar imediatamente:\n")
print("insira aqui a quantidade de Hospitais desejada e aperte enter:")
qtd_de_hospitais = int(input())


# Criando filas, uma pra cada nivel de urgencia e idade
Neonatal_Urg = Classes.cFila()
Neonatal_mt_Urg = Classes.cFila()
Neonatal_Emerg = Classes.cFila()

Pediatrico_Urg = Classes.cFila()
Pediatrico_mt_Urg = Classes.cFila()
Pediatrico_Emerg = Classes.cFila()

Adulto_Urg = Classes.cFila()
Adulto_mt_Urg = Classes.cFila()
Adulto_Emerg = Classes.cFila()


# Criando Pilhas
Leitos_Neonatal = Classes.cPilha()
Leitos_Pediatrico = Classes.cPilha()
Leitos_Adulto = Classes.cPilha()


# ============= INÍCIO DA SIMULAÇÃO =============

while True:
    print("\n_______________________________\n")

    # Organizando as filas
    novos_pacientes = random.randint(1, 40)
    for i in range (novos_pacientes):
        paciente = Classes.cPaciente()
        ## Neonatal
        if paciente.idade == 0:  
            if paciente.gravidade == 1:
                Neonatal_Urg.enfileirar(paciente)

            if paciente.gravidade == 2:
                Neonatal_mt_Urg.enfileirar(paciente)

            if paciente.gravidade == 3:
                Neonatal_Emerg.enfileirar(paciente)

        ## Pediátrico
        if paciente.idade >= 1 and paciente.idade <= 13:
            if paciente.gravidade == 1:
                Pediatrico_Urg.enfileirar(paciente)
        
            if paciente.gravidade == 2:
                Pediatrico_mt_Urg.enfileirar(paciente)

            if paciente.gravidade == 3:
                Pediatrico_Emerg.enfileirar(paciente)

        ## Adulto
        if paciente.idade > 13:
            if paciente.gravidade == 1:
                Adulto_Urg.enfileirar(paciente)

            if paciente.gravidade == 2:
                Adulto_mt_Urg.enfileirar(paciente)

            if paciente.gravidade == 3:
                Adulto_Emerg.enfileirar(paciente)


    # Organizando as pilhas de leitos
    novos_leitos = random.randint(1, 30)
    for i in range (novos_leitos):
        leito = Classes.cLeito(qtd_de_hospitais)

        if leito.tipo <= 4:
            Leitos_Neonatal.push(leito)

        if leito.tipo > 4 and leito.tipo <= 13:
            Leitos_Pediatrico.push(leito)

        if leito.tipo > 13:
            Leitos_Adulto.push(leito)

    print(f"Novos Pacientes: {novos_pacientes}\n")
    print(f"Novos Leitos: {novos_leitos}\n")

    # Contadores
    leitos_alocados = 0   # mesma coisa que qtd de pacientes atendidos
    leitos_disponiveis = Leitos_Neonatal.getTamanho() + Leitos_Pediatrico.getTamanho() + Leitos_Adulto.getTamanho()
    lista_de_espera = Neonatal_Urg.getTamanho() + Neonatal_mt_Urg.getTamanho() + Neonatal_Emerg.getTamanho() + Pediatrico_Urg.getTamanho() + Pediatrico_mt_Urg.getTamanho() + Pediatrico_Emerg.getTamanho() + Adulto_Urg.getTamanho() + Adulto_mt_Urg.getTamanho() + Adulto_Emerg.getTamanho()
    mortes = 0
    piora_gravidade = 0
    melhora_gravidade = 0
    curados = 0
    # ============= MAPA INICIAL =============
    print("\n========= Status Pré-Alocação =========\n")
    print(f"Leitos Alocados (Pacientes atendidos): {leitos_alocados}\n")
    print(f"Leitos Disponíveis: {leitos_disponiveis}\n")
    print(f"Quantidade de pacientes na lista de espera: {lista_de_espera}\n")

    print(f"==== Distribuição dos Pacientes ====\n")
    print(f"Neonatal:\n Emergência: {Neonatal_Emerg.getTamanho()}                 Muito Urgente: {Neonatal_mt_Urg.getTamanho()}                 Urgente: {Neonatal_Urg.getTamanho()}\n")
    print(f"Pediátrico:\n Emergência: {Pediatrico_Emerg.getTamanho()}                 Muito Urgente: {Pediatrico_mt_Urg.getTamanho()}                 Urgente: {Pediatrico_Urg.getTamanho()}\n")
    print(f"Adulto:\n Emergência: {Adulto_Emerg.getTamanho()}                 Muito Urgente: {Adulto_mt_Urg.getTamanho()}                 Urgente: {Adulto_Urg.getTamanho()}\n")


    print(f"==== Distribuição dos Leitos ====\n")
    print(f"Neonatal: {Leitos_Neonatal.getTamanho()}\n")
    print(f"Pediátrico: {Leitos_Pediatrico.getTamanho()}\n")
    print(f"Adulto: {Leitos_Adulto.getTamanho()}\n")




    #  ============= Alocação de Leitos =============

    print("\n========= OPERAÇÕES REALIZADAS =========\n")
    ## Neonatal:
    while Leitos_Neonatal.empty() == False:
        if Neonatal_Emerg.empty() == False:
            print(f"Movendo paciente de id {Neonatal_Emerg.inicio.dado.id} para o leito neoatal {Leitos_Neonatal.top.dado.id} do hospital {Leitos_Neonatal.top.dado.hospital}\n")
            Neonatal_Emerg.desenfileirar()
            Leitos_Neonatal.pop()
            leitos_alocados += 1

        else:
            if Neonatal_mt_Urg.empty() == False:
                print(f"Movendo paciente de id {Neonatal_mt_Urg.inicio.dado.id} para o leito neoatal {Leitos_Neonatal.top.dado.id} do hospital {Leitos_Neonatal.top.dado.hospital}\n")
                Neonatal_mt_Urg.desenfileirar()
                Leitos_Neonatal.pop()
                leitos_alocados += 1

            else:
                if Neonatal_Urg.empty() == False:
                    print(f"Movendo paciente de id {Neonatal_Urg.inicio.dado.id} para o leito neoatal {Leitos_Neonatal.top.dado.id} do hospital {Leitos_Neonatal.top.dado.hospital}\n")
                    Neonatal_Urg.desenfileirar()
                    Leitos_Neonatal.pop()
                    leitos_alocados += 1
        
        if Neonatal_Emerg.empty() == True and Neonatal_mt_Urg.empty() == True and Neonatal_Urg.empty() == True:
            break

    ## Pediátrico
    while Leitos_Pediatrico.empty() == False:
        if Pediatrico_Emerg.empty() == False:
            print(f"Movendo paciente de id {Pediatrico_Emerg.inicio.dado.id} para o leito pediátrico {Leitos_Pediatrico.top.dado.id} do hospital {Leitos_Pediatrico.top.dado.hospital}\n")
            Pediatrico_Emerg.desenfileirar()
            Leitos_Pediatrico.pop()
            leitos_alocados += 1
        
        else:
            if Pediatrico_mt_Urg.empty() == False:
                print(f"Movendo paciente de id {Pediatrico_mt_Urg.inicio.dado.id} para o leito pediátrico {Leitos_Pediatrico.top.dado.id} do hospital {Leitos_Pediatrico.top.dado.hospital}\n")
                Pediatrico_mt_Urg.desenfileirar()
                Leitos_Pediatrico.pop()
                leitos_alocados += 1

            else:
                if Pediatrico_Urg.empty() == False:
                    print(f"Movendo paciente de id {Pediatrico_Urg.inicio.dado.id} para o leito pediátrico {Leitos_Pediatrico.top.dado.id} do hospital {Leitos_Pediatrico.top.dado.hospital}\n")
                    Pediatrico_Urg.desenfileirar()
                    Leitos_Pediatrico.pop()
                    leitos_alocados += 1

        if Pediatrico_Emerg.empty() == True and Pediatrico_mt_Urg.empty() == True and Pediatrico_Urg.empty() == True:
            break

    ## Adulto
    while Leitos_Adulto.empty() == False:
        if Adulto_Emerg.empty() == False:
            print(f"Movendo paciente de id {Adulto_Emerg.inicio.dado.id} para o leito adulto {Leitos_Adulto.top.dado.id} do hospital {Leitos_Adulto.top.dado.hospital}\n")
            Adulto_Emerg.desenfileirar()
            Leitos_Adulto.pop()
            leitos_alocados += 1
        
        else:
            if Adulto_mt_Urg.empty() == False:
                print(f"Movendo paciente de id {Adulto_mt_Urg.inicio.dado.id} para o leito adulto {Leitos_Adulto.top.dado.id} do hospital {Leitos_Adulto.top.dado.hospital}\n")
                Adulto_mt_Urg.desenfileirar()
                Leitos_Adulto.pop()
                leitos_alocados += 1
            
            else:
                if Adulto_Urg.empty() == False:
                    print(f"Movendo paciente de id {Adulto_Urg.inicio.dado.id} para o leito adulto {Leitos_Adulto.top.dado.id} do hospital {Leitos_Adulto.top.dado.hospital}\n")
                    Adulto_Urg.desenfileirar()
                    Leitos_Adulto.pop()
                    leitos_alocados += 1
        if Adulto_Emerg.empty() == True and Adulto_mt_Urg.empty() == True and Adulto_Urg.empty() == True:
            break



    # ============= SAÍDA =============

    ## procurar mudanças de estado - NAO FUNCIONA PQ A REMOÇÃO NAO FUNCIONA
    noAtual = Neonatal_Urg.inicio
    for i in range (Neonatal_Urg.getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Neonatal_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            piora_gravidade += 1
            sorteio = random.randint(2,3)
            if sorteio == 2:
                noAtual.dado.tipo = 2
                Neonatal_mt_Urg.enfileirar(noAtual)
                Neonatal_Urg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 3
                Neonatal_Emerg.enfileirar(noAtual)
                Neonatal_Urg.remover(noAtual)

        if mudança_estado > 15 and mudança_estado <= 25:
            Neonatal_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Neonatal_Urg.remover(noAtual)
            curados += 1

        noAtual = Neonatal_Urg.inicio.prox
    

    noAtual = Neonatal_mt_Urg.inicio
    for i in range(Neonatal_mt_Urg.getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Neonatal_mt_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            noAtual.dado.tipo = 3
            Neonatal_Emerg.enfileirar(noAtual)
            Neonatal_mt_Urg.remover(noAtual)
            piora_gravidade += 1

        if mudança_estado > 15 and mudança_estado <= 25:
            noAtual.dado.tipo = 1
            Neonatal_Urg.enfileirar(noAtual)
            Neonatal_mt_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Neonatal_mt_Urg.remover(noAtual)
            curados += 1

        noAtual = Neonatal_mt_Urg.inicio.prox

    
    noAtual = Neonatal_Emerg.inicio
    for i in range(Neonatal_Emerg .getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Neonatal_Emerg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 15 and mudança_estado <= 25:
            melhora_gravidade += 1
            sorteio = random.randint(1,2)
            if sorteio == 1:
                noAtual.dado.tipo = 1
                Neonatal_Urg.enfileirar(noAtual)
                Neonatal_Emerg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 2
                Neonatal_mt_Urg.enfileirar(noAtual)
                Neonatal_Emerg.remover(noAtual)

        if mudança_estado > 25 and mudança_estado <=30:
            Neonatal_Emerg.remover(noAtual)
            curados += 1

        noAtual = Neonatal_Emerg.inicio.prox

    
    noAtual = Pediatrico_Urg.inicio
    for i in range(Pediatrico_Urg .getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Pediatrico_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            piora_gravidade += 1
            sorteio = random.randint(2,3)
            if sorteio == 2:
                noAtual.dado.tipo = 2
                Pediatrico_mt_Urg.enfileirar(noAtual)
                Pediatrico_Urg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 3
                Pediatrico_Emerg.enfileirar(noAtual)
                Pediatrico_Urg.remover(noAtual)

        if mudança_estado > 15 and mudança_estado <= 25:
            Pediatrico_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Pediatrico_Urg.remover(noAtual)
            curados += 1

        noAtual = Pediatrico_Urg.inicio.prox

    
    noAtual = Pediatrico_mt_Urg.inicio
    for i in range(Pediatrico_mt_Urg.getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Pediatrico_mt_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            noAtual.dado.tipo = 3
            Pediatrico_Emerg.enfileirar(noAtual)
            Pediatrico_mt_Urg.remover(noAtual)
            piora_gravidade += 1

        if mudança_estado > 15 and mudança_estado <= 25:
            noAtual.dado.tipo = 1
            Pediatrico_Urg.enfileirar(noAtual)
            Pediatrico_mt_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Pediatrico_mt_Urg.remover(noAtual)
            curados += 1

        noAtual = Pediatrico_mt_Urg.inicio.prox

    
    noAtual = Pediatrico_Emerg.inicio
    for i in range(Pediatrico_Emerg.getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Pediatrico_Emerg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 15 and mudança_estado <= 25:
            melhora_gravidade += 1
            sorteio = random.randint(1,2)
            if sorteio == 1:
                noAtual.dado.tipo = 1
                Pediatrico_Urg.enfileirar(noAtual)
                Pediatrico_Emerg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 2
                Pediatrico_mt_Urg.enfileirar(noAtual)
                Pediatrico_Emerg.remover(noAtual)

        if mudança_estado > 25 and mudança_estado <=30:
            Pediatrico_Emerg.remover(noAtual)
            curados += 1

        noAtual = Pediatrico_Emerg.inicio.prox


    noAtual = Pediatrico_Urg.inicio
    for i in range(Adulto_Urg .getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Adulto_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            piora_gravidade += 1
            sorteio = random.randint(2,3)
            if sorteio == 2:
                noAtual.dado.tipo = 2
                Adulto_mt_Urg.enfileirar(noAtual)
                Adulto_Urg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 3
                Adulto_Emerg.enfileirar(noAtual)
                Adulto_Urg.remover(noAtual)

        if mudança_estado > 15 and mudança_estado <= 25:
            Adulto_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Adulto_Urg.remover(noAtual)
            curados += 1

        noAtual = Adulto_Urg.inicio.prox


    noAtual = Adulto_mt_Urg.inicio
    for i in range(Adulto_mt_Urg.getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Adulto_mt_Urg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 5 and mudança_estado <= 15:
            noAtual.dado.tipo = 3
            Adulto_Emerg.enfileirar(noAtual)
            Adulto_mt_Urg.remover(noAtual)
            piora_gravidade += 1

        if mudança_estado > 15 and mudança_estado <= 25:
            noAtual.dado.tipo = 1
            Adulto_Urg.enfileirar(noAtual)
            Adulto_mt_Urg.remover(noAtual)
            melhora_gravidade += 1

        if mudança_estado > 25 and mudança_estado <=30:
            Adulto_mt_Urg.remover(noAtual)
            curados += 1

        noAtual = Adulto_mt_Urg.inicio.prox


    noAtual = Adulto_Emerg.inicio
    for i in range(Adulto_Emerg .getTamanho()):
        mudança_estado = random.randint(1, 100)
        if mudança_estado <= 5:
            Adulto_Emerg.remover(noAtual)
            mortes += 1
        
        if mudança_estado > 15 and mudança_estado <= 25:
            melhora_gravidade += 1
            sorteio = random.randint(1,2)
            if sorteio == 1:
                noAtual.dado.tipo = 1
                Adulto_Urg.enfileirar(noAtual)
                Adulto_Emerg.remover(noAtual)
                
            else:
                noAtual.dado.tipo = 2
                Adulto_mt_Urg.enfileirar(noAtual)
                Adulto_Emerg.remover(noAtual)

        if mudança_estado > 25 and mudança_estado <=30:
            Adulto_Emerg.remover(noAtual)
            curados += 1

        noAtual = Adulto_Emerg.inicio.prox




    leitos_disponiveis -= leitos_alocados
    lista_de_espera -= leitos_alocados

    print("\n========= Status Pós-Alocação =========\n")
    print(f"Leitos Alocados (Pacientes atendidos): {leitos_alocados}\n")
    print(f"Leitos Disponíveis: {leitos_disponiveis}\n")
    print(f"Quantidade de pacientes na lista de espera: {lista_de_espera}\n")
    print(f"Pacientes que vieram a falecer: {mortes}\n")
    print(f"Pacientes que foram curados: {curados}\n")
    print(f"Pacientes que tiveram melhoria na gravidade: {melhora_gravidade}\n")
    print(f"Pacientes que tiveram piora na gravidade: {piora_gravidade}\n")
    

    print(f"==== Distribuição dos Pacientes ====\n")
    print(f"Neonatal:\n Emergência: {Neonatal_Emerg.getTamanho()}                 Muito Urgente: {Neonatal_mt_Urg.getTamanho()}                 Urgente: {Neonatal_Urg.getTamanho()}\n")
    print(f"Pediátrico:\n Emergência: {Pediatrico_Emerg.getTamanho()}                 Muito Urgente: {Pediatrico_mt_Urg.getTamanho()}                 Urgente: {Pediatrico_Urg.getTamanho()}\n")
    print(f"Adulto:\n Emergência: {Adulto_Emerg.getTamanho()}                 Muito Urgente: {Adulto_mt_Urg.getTamanho()}                 Urgente: {Adulto_Urg.getTamanho()}\n")

    print(f"==== Distribuição dos Leitos ====\n")
    print(f"Neonatal: {Leitos_Neonatal.getTamanho()}\n")
    print(f"Pediátrico: {Leitos_Pediatrico.getTamanho()}\n")
    print(f"Adulto: {Leitos_Adulto.getTamanho()}\n")


    if leitos_disponiveis == 0:
        print("* ATENÇÃO: sistema sobrecarregado! não há leitos disponíveis! Medidas urgentes precisam ser tomadas.\n")

    else:
        if Leitos_Neonatal.getTamanho() == 0:
            print("* ATENÇÃO: Não há leitos Neonatais disponíveis! Medidas precisam ser tomadas.\n")

        if Leitos_Pediatrico.getTamanho() == 0:
            print("* ATENÇÃO: Não há leitos Pediátricos disponíveis! Medidas precisam ser tomadas.\n")

        if Leitos_Adulto.getTamanho() == 0:
            print("* ATENÇÃO: Não há leitos Adultos disponíveis! Medidas precisam ser tomadas.\n")

        if Leitos_Neonatal.getTamanho() > 0 and Leitos_Pediatrico.getTamanho() > 0 and Leitos_Adulto.getTamanho() > 0:
            print("* Aviso: o sistema possui leitos disponíveis para receberem mais pacientes.\n")
    

    print("_______________________________\n")
    print("A simulação deste evento acabou. Deseja continuar? Se sim, digite 'continuar' e aperte enter. Se não, digite 'encerrar'. (sem as aspas e usando letras minúsculas) \n")
    
    tecla = input()
    if tecla == "continuar":
        print("\nCerto!\n")
        print("Novos pacientes e leitos chegando:\n")
        print("\n========================================================")
        print("========================================================")
        print("========================================================")
        print("========================================================\n")
        continue
    if tecla == "encerrar":
        print("\nSimulação encerrada. Obrigado e volte sempre!\n")
        break