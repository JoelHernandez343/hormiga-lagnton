class Matriz:
    def __init__(self, ancho=0, altura=0, matriz=None):

        if matriz is None:
            self.ancho = ancho
            self.altura = altura
            self.matriz = [[0 for j in range(ancho)] for i in range(altura)]
        else:
            self.ancho = len(matriz[0])
            self.altura = len(matriz)
            self.matriz = matriz

    def obt_color_casilla(self, posicion):
        x, y = posicion
        return self.matriz[y][x]

    def est_color_casilla(self, posicion, color):
        x, y = posicion
        self.matriz[y][x] = color
