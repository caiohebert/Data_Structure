import Classes
import pyglet
from pyglet import shapes
from pyglet.window import key


# ============ INÍCIO ============
print("\nBem vindo ao Visualizador!\nAperte a tecla correspondente a inicial do grafico que deseja visualizar\n")
print("1) Infinito (tecla i)\n2) Laço (tecla l)\n3) Cardioide (tecla c)\n")
print("utilize as teclas 1 e 3 para mudar o modo de visualização da sua função e a teclas 4, 6, 8 e 9 para mudar o nível de refinamento\n")

print("ATENÇÃO: o refinamento da tecla 9 pode demorar um pouquinho, mas funciona!\n")


# ============ CRIAÇÃO DA JANELA DE VISUALIZAÇÃO ============
# dimensão de 500 x 500

window = pyglet.window.Window(500, 500)
window.set_caption('Visualização da Curva Implicita')



# ============ CRIAÇÃO DA FIGURA ============
arvore = Classes.cQuadTree(500, 500)    
# parâmetros: refinamento, tipo de equação, tipo de visualização

arvore.CriarImagem(11, 3, 1)

equacao = 3
modo = 1
refinamento = 11

@window.event
def on_key_press(symbol, modifiers):
    global equacao, modo, refinamento
    # imprime a função do cardioide ao apertar a tecla "C"
    if symbol == key.C:
        equacao = 3

    # imprime a função do infinito ao apertar a tecla "I"
    if symbol == key.I:
        equacao = 1

    # imprime a função do Laço ao apertar a tecla "L"
    if symbol == key.L:
        equacao = 2

    # Modo 1 ao apertar a tecla "1"
    if symbol == key.NUM_1:
        modo = 1

    # Modo 3 ao apertar a tecla "3"
    if symbol == key.NUM_3:
        modo = 3

    # altera os niveis de detalhamento
    if symbol == key.NUM_4:
        refinamento = 4

    if symbol == key.NUM_6:
        refinamento = 6
        
    if symbol == key.NUM_8:
        refinamento = 8

    if symbol == key.NUM_9:
        refinamento = 11

    arvore.CriarImagem(refinamento, equacao, modo)


# ============ DETALHES FINAIS ============
@window.event
def on_draw():
    window.clear()
    Classes.batch.draw()

pyglet.app.run()
