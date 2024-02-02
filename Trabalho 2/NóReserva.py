class cNo:
    def __init__(self, dado = None):
        self.__dado__ = dado
        self.__prox__ = None

# *******************************************************
# ***                                                 ***
# *******************************************************

    def setDado(self, dado):

        # if type(dado) == int:
            self.__dado__ = dado

# *******************************************************
# ***                                                 ***
# *******************************************************

    def setProx(self, prox):

        # if type(prox) == cNo:
            self.__prox__ = prox

# *******************************************************
# ***                                                 ***
# *******************************************************

    def getDado(self):
        return self.__dado__

# *******************************************************
# ***                                                 ***
# *******************************************************

    def getProx(self):
        return self.__prox__ 


# *******************************************************
# ***                                                 ***
# *******************************************************


    def __str__(self):
      outStr = ""
      outStr += "Dado:" + str(self.dado) + " " + "Próximo:" + str(self.prox) 
      return outStr


class fila:
  def __init__ (self):
    self.front = None
    self.rear = None
  
# *******************************************************
# ***                                                 ***
# *******************************************************

  def Enqueue (self, n):
    novoNo = cNo(n)
    if self.front == None:
      self.front = novoNo
      self.rear = novoNo
    
    else:
      noCorrente = self.front
      while noCorrente.getProx() != None:
          noCorrente = noCorrente.getProx()

      noCorrente.setProx(novoNo)
      self.rear = novoNo


    
# *******************************************************
# ***                                                 ***
# *******************************************************

  def Dequeue (self):
    if self.front == None:
      return False
    
    noCorrente = self.front
    noPosterior = noCorrente.getProx()

    del noCorrente
    self.front = noPosterior
        
    return True

# *******************************************************
# ***                                                 ***
# *******************************************************

  def empty (self):
    if self.top == None:
      return True

    return False


  def __str__(self):
    outStr = ""

    noCorrente = self.front

    if noCorrente == None:        
        outStr += "=====================\n"
        outStr += "|   LISTA   VAZIA   |\n"
        outStr += "=====================\n"
    else:
        while noCorrente != None:
            outStr += str(noCorrente.getDado()) + " "
            noCorrente = noCorrente.getProx()
    return outStr


fila1 = fila()
fila1.Enqueue(2)
fila1.Enqueue(5)
print(fila1.__str__())