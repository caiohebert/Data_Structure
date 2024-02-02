import pyglet
from pyglet import shapes
from pyglet import key
window = pyglet.window.Window(500, 500)
batch = pyglet.graphics.Batch()


retb = shapes.BorderedRectangle(250, 300, 400, 200, border=4, color=(255, 255, 255), border_color=(200, 0, 0), batch=batch, group=None)
retb1 = shapes.BorderedRectangle(250, 300, 200, 100, border=4, color=(0, 0, 0), border_color=(200, 0, 0), batch=batch, group=None)

retb1.opacity = 50

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()



if tipo == 2:
    # imprime em azul se for positivo
    if valor_NE > 0 and valor_SE > 0 and valor_SO > 0 and valor_NO > 0:
        quadrado = shapes.BorderedRectangle(self.F_Nordeste.x, self.F_Nordeste.y, self.F_Nordeste.largura, self.F_Nordeste.altura, border = 1.5, color=(0, 0, 255), border_color=(0, 0, 255), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Sudeste.x, self.F_Sudeste.y, self.F_Sudeste.largura, self.F_Sudeste.altura, border = 1.5, color=(0, 0, 255), border_color=(0, 0, 255), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Sudoeste.x, self.F_Sudoeste.y, self.F_Sudoeste.largura, self.F_Sudoeste.altura, border = 1.5, color=(0, 0, 255), border_color=(0, 0, 255), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Noroeste.x, self.F_Noroeste.y, self.F_Noroeste.largura, self.F_Noroeste.altura, border = 1.5, color=(0, 0, 255), border_color=(0, 0, 255), batch=batch, group=None)
        shapeList.append(quadrado)

    # imprime em vermelho se negativo
    if valor_NE < 0 and valor_SE < 0 and valor_SO < 0 and valor_NO < 0:
        quadrado = shapes.BorderedRectangle(self.F_Nordeste.x, self.F_Nordeste.y, self.F_Nordeste.largura, self.F_Nordeste.altura, border = 1.5, color=(255, 0, 0), border_color=(255, 0, 0), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Sudeste.x, self.F_Sudeste.y, self.F_Sudeste.largura, self.F_Sudeste.altura, border = 1.5, color=(255, 0, 0), border_color=(255, 0, 0), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Sudoeste.x, self.F_Sudoeste.y, self.F_Sudoeste.largura, self.F_Sudoeste.altura, border = 1.5, color=(255, 0, 0), border_color=(255, 0, 0), batch=batch, group=None)
        shapeList.append(quadrado)

        quadrado = shapes.BorderedRectangle(self.F_Noroeste.x, self.F_Noroeste.y, self.F_Noroeste.largura, self.F_Noroeste.altura, border = 1.5, color=(255, 0, 0), border_color=(255, 0, 0), batch=batch, group=None)
        shapeList.append(quadrado)
