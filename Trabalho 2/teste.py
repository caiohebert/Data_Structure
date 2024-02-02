# ####################################################################
# Demo para controle de desenho e eventos de teclado usando o PyGlet #
# ####################################################################

import sys
import random
from datetime       import datetime

import pyglet
from pyglet         import shapes
from pyglet.window  import Window
from pyglet.window  import key

WIN_X       = 800
WIN_Y       = 800

drawRetas   = False
drawQuads   = False
retas       = None
quads       = None

cores =     [   (255,   0,   0), 
                (  0, 255,   0), 
                (255,   0, 255), 
                (255, 255,   0), 
                (255,   0, 255),
                (  0, 255, 255),  
                (255, 255, 255)  
            ]

# *******************************************************
# ***                                                 ***
# *******************************************************
def montaLista(tipo):

    batch           = pyglet.graphics.Batch()
    shapeList       = []

    if tipo == "RETAS":

        for i in range(0, 10):
            iCor = i % 7

            x0 = random.randint(10, 400)
            y0 = random.randint(10, 400)

            x1 = random.randint(410, 790)
            y1 = random.randint(410, 790)

            shapeList.append(shapes.Line(x0, y0, x1, y1, width=2, color=cores[iCor], batch=batch))

    elif tipo == "QUADS":
        for i in range(0, 10):
            iCor = i % 7

            x = random.randint(10, 790)
            y = random.randint(10, 790)

            w = random.randint(80, 400)
            h = random.randint(80, 400)
            if i % 2:
                shapeList.append(shapes.Rectangle( x, y, w, h, color=cores[iCor], batch=batch ) )
            else:
                shapeList.append(shapes.BorderedRectangle( x, y, w, h, border_color=cores[iCor], color=(0,0,0), batch=batch ) )


    return batch, shapeList

# *******************************************************
# ***                                                 ***
# *******************************************************
def gameLoop():

    global window, retas, quads

    window          = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption('Visualiza Curva Implicita')

    def on_draw():

        global drawRetas, drawQuads

        window.clear()

        if drawRetas:
            retas.draw()
    
        if drawQuads:
            quads.draw()

    window.push_handlers(on_draw)

    def on_key_press(symbol, modifiers):      

        global drawRetas, drawQuads, retas, quads, sR, sQ

        if symbol == pyglet.window.key.C:       # Pressionando C para gerar os desenhos
            if retas == None:
                retas, sR = montaLista("RETAS")
                drawRetas = True

            if quads == None:
                quads, sQ = montaLista("QUADS")
                drawQuads = True

        elif symbol == pyglet.window.key.R:     # Pressionando R para ligar ou desligar o desenho das retas
            if retas:
                drawRetas = not drawRetas
    
        elif symbol == pyglet.window.key.Q:     # Pressionando Q para ligar ou desligar o desenho dos quadrados
            if quads:
                drawQuads = not drawQuads

    window.push_handlers(on_key_press)

    pyglet.app.run()

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if (len(sys.argv) > 1):
        MAX_LEVEL = int(sys.argv[1])

    gameLoop()





    