import pyglet
from pyglet import shapes
batch = pyglet.graphics.Batch()
shapeList = []
# ============ NÓ ============
class cNo:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        # sub-arvores
        self.F_Nordeste = None
        self.F_Sudeste = None
        self.F_Sudoeste = None
        self.F_Noroeste = None

    #________________________________

    def Resolver_eq(self, equacao, x, y):
        coord_x = (x - 250)/50              # montar um plano cartesiano com origem no centro da janela
        coord_y = (y - 250)/50
        if equacao == 1:
            # Infinito
            resultado = (coord_x**2 + coord_y**2)**2 - 25*(coord_x**2 - coord_y**2)
            return resultado

        if equacao == 2:
            # Laço
            resultado = coord_x**7 - coord_y**5 + coord_x**2 * coord_y**3 - (coord_x*coord_y)**2
            return resultado

        if equacao == 3:
            # cardioide
            resultado = (coord_x**2 + coord_y**2 - 4)**3 - coord_x**2 * coord_y**3
            return resultado

    #________________________________


    def ContemPonto(self, equacao, tipo):
        # verificar se algum vertice do quadrado tem sinal oposto aos demais
        valor_NE = self.Resolver_eq(equacao, self.x + self.largura, self.y + self.altura)
        valor_SE = self.Resolver_eq(equacao, self.x + self.largura, self.y)
        valor_SO = self.Resolver_eq(equacao, self.x, self.y)
        valor_NO = self.Resolver_eq(equacao, self.x, self.y + self.altura)


        if valor_NE == valor_SE or valor_NO == valor_SO:
            return True

        if (valor_NE > 0 and valor_SE > 0 and valor_SO > 0 and valor_NO > 0) or (valor_NE < 0 and valor_SE < 0 and valor_SO < 0 and valor_NO < 0):
            return False
        
        return True

    #________________________________

    def Subdividir(self, limite_ref, equacao, nivel, tipo):
        nivel += 1
        if nivel == limite_ref:
            # pinta o quadrado de acordo com o tipo de visualização escolhida
            if (tipo == 1):
                # quadrados finais em cinza e fundo preto
                quadrado = shapes.BorderedRectangle(self.x, self.y, self.largura, self.altura, border = 1.5, color=(128,128,128), border_color=(128,128,128), batch=batch, group=None)
                shapeList.append(quadrado)

            if (tipo == 3):
                # apenas as bordas dos quadrados
                quadrado = shapes.BorderedRectangle(self.x, self.y, self.largura, self.altura, border = 1.5, color=(0, 0, 0), border_color=(0, 0, 0), batch=batch, group=None)
                quadrado.opacity = 0
                shapeList.append(quadrado)

            #faz as folhas apontarem para None
            self.F_Nordeste = None
            self.F_Sudeste = None
            self.F_Sudoeste = None
            self.F_Noroeste = None
            return

        self.F_Nordeste = cNo(self.x + self.largura/2, self.y + self.altura/2, self.largura/2, self.altura/2)
        self.F_Sudeste = cNo(self.x + self.largura/2, self.y, self.largura/2, self.altura/2)
        self.F_Sudoeste = cNo(self.x, self.y, self.largura/2, self.altura/2)
        self.F_Noroeste = cNo(self.x, self.y + self.altura/2, self.largura/2, self.altura/2)

        
        # não imprime quadrados intermediarios no tipo 1
        if (tipo == 3):
            quadrado = shapes.BorderedRectangle(self.F_Nordeste.x, self.F_Nordeste.y, self.F_Nordeste.largura, self.F_Nordeste.altura, border = 1.5, color=(255, 255, 255), border_color=(0, 0, 0), batch=batch, group=None)
            quadrado.opacity = 0
            shapeList.append(quadrado)

            quadrado = shapes.BorderedRectangle(self.F_Sudeste.x, self.F_Sudeste.y, self.F_Sudeste.largura, self.F_Sudeste.altura, border = 1.5, color=(255, 255, 255), border_color=(0, 0, 0), batch=batch, group=None)
            quadrado.opacity = 0
            shapeList.append(quadrado)

            quadrado = shapes.BorderedRectangle(self.F_Sudoeste.x, self.F_Sudoeste.y, self.F_Sudoeste.largura, self.F_Sudoeste.altura, border = 1.5, color=(255, 255, 255), border_color=(0, 0, 0), batch=batch, group=None)
            quadrado.opacity = 0
            shapeList.append(quadrado)

            quadrado = shapes.BorderedRectangle(self.F_Noroeste.x, self.F_Noroeste.y, self.F_Noroeste.largura, self.F_Noroeste.altura, border = 1.5, color=(255, 255, 255), border_color=(0, 0, 0), batch=batch, group=None)
            quadrado.opacity = 0
            shapeList.append(quadrado)


        if self.F_Nordeste.ContemPonto(equacao, tipo) == True:
            self.F_Nordeste.Subdividir(limite_ref, equacao, nivel, tipo)

        if self.F_Sudeste.ContemPonto(equacao, tipo) == True:
            self.F_Sudeste.Subdividir(limite_ref, equacao, nivel, tipo)

        if self.F_Sudoeste.ContemPonto(equacao, tipo) == True:
            self.F_Sudoeste.Subdividir(limite_ref, equacao, nivel, tipo)

        if self.F_Noroeste.ContemPonto(equacao, tipo) == True:
            self.F_Noroeste.Subdividir(limite_ref, equacao, nivel, tipo)



# ============ QUADTREE ============
class cQuadTree:
    def __init__(self, larg_T, altura_T):
        self.raiz = None
        self.larg_T = larg_T
        self.altura_T = altura_T
        self.nivel = 0
        
    #________________________________

    def CriarImagem(self, limite_ref, equacao, tipo):
        nivel = 0
        No = cNo(0, 0, self.larg_T, self.altura_T)
        self.raiz = No

        # imprimir quadrado inicial (fundo)
        if (tipo == 1):
            quadrado = shapes.BorderedRectangle(self.raiz.x, self.raiz.y, self.raiz.largura, self.raiz.altura, border = 1.5, color=(0, 0, 0), border_color=(0, 0, 0), batch=batch, group=None)
            shapeList.append(quadrado)

        if (tipo == 3):
            quadrado = shapes.BorderedRectangle(self.raiz.x, self.raiz.y, self.raiz.largura, self.raiz.altura, border = 1.5, color=(255, 255, 255), border_color=(0, 0, 0), batch=batch, group=None)
            shapeList.append(quadrado)
        self.raiz.Subdividir(limite_ref, equacao, nivel, tipo)
        
