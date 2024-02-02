import random
# ============ PACIENTE ============
class cPaciente:
    def __init__(self):
        self.idade = random.randint(0, 94)           
        self.gravidade = random.randint(1, 3)
        # 1 = Urgente, 2 = muito urgente, 3 = emergência
        self.id = random.randint(1, 100000)

        


# ============ LEITO ============
class cLeito:
    def __init__(self, n):
        self.id =  random.randint(1, 1000)
        self.tipo = random.randint(1, 50)     
        # 1-4 = neonatal, 4-13 = pediatrico, 14-50 = adulto. Usei esses números para diminuir a probabilidade de aparecer leitos de neonatal.
        self.hospital = random.randint(1, n)



# ============ NÓ ============
class cNo:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    #________________________________

    def __str__(self):
      outStr = ""
      outStr += "Dado:" + str(self.dado) + " " + "Próximo:" + str(self.prox) 
      return outStr
    
    


# ============ FILA ============
class cFila:
    def __init__ (self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    #________________________________

    def enfileirar (self, n):
        novoNo = cNo(n)
        if self.inicio == None:
            self.inicio = novoNo
            self.fim = novoNo

        else:
            self.fim.prox = novoNo
            self.fim = novoNo

        self.tamanho += 1

    #________________________________

    def desenfileirar (self):
        if self.inicio == None:
            return False

        noCorrente = self.inicio
        self.inicio = self.inicio.prox

        del noCorrente
        self.tamanho -= 1

        return True

    #________________________________

    def empty (self):
        if self.inicio == None:
            return True

        return False

    #________________________________

    def getTamanho(self):
        return self.tamanho

    #________________________________

    def remover(self, n):
        if self.inicio == None:
            return False
        
        noAnterior = None
        noCorrente = self.inicio
        
        while noCorrente != n:
            noAnterior = noCorrente
            noCorrente = noCorrente.prox

        if noAnterior == None:
            self.inicio = noCorrente.prox

        if noCorrente.prox == None:
            noAnterior.prox = None
        
        if noAnterior != None and noCorrente.prox != None:
            noAnterior.prox = noCorrente.prox
        
        del noCorrente
        self.tamanho -= 1

        return True

    #________________________________

    def __str__(self):
        outStr = ""
        noCorrente = self.inicio

        if noCorrente == None:        
            outStr += "=====================\n"
            outStr += "|    FILA  VAZIA    |\n"
            outStr += "=====================\n"
        else:
            while noCorrente != None:
                outStr += str(noCorrente.dado) + " "
                noCorrente = noCorrente.prox

        return outStr

    #________________________________
    def busca (self,n):
        noCorrente = self.inicio
        for i in range (self.getTamanho()):
            if noCorrente.dado == n:
                return True
            noCorrente = noCorrente.prox
        return False


# ============ PILHA ============
class cPilha:
    def __init__ (self):
        self.top = None       
        self.tamanho = 0
    #________________________________

    def push (self, n):
        novoNo = cNo(n)
        if self.top == None:
            self.top = novoNo
        else:
            novoNo.prox = self.top
            self.top = novoNo
        
        self.tamanho += 1
    #________________________________

    def pop (self):
        if self.top == None:
            return False

        topoAntigo = self.top
        self.top = self.top.prox
        del topoAntigo
        self.tamanho -= 1

        return True

    #________________________________

    def empty (self):
        if self.top == None:
            return True

        return False

    #________________________________

    def __str__ (self):
        outStr = ""
        noCorrente = self.top
        if noCorrente == None:        
            outStr += "=====================\n"
            outStr += "|    PILHA VAZIA    |\n"
            outStr += "=====================\n"
        else:
            while noCorrente != None:
                outStr += str(noCorrente.dado) + " "
                noCorrente = noCorrente.prox

        return outStr
    
    #________________________________

    def getTamanho(self):
        return self.tamanho