class Hormiga:
    def __init__(self, posicion, orientacion, color):
        self.posicion = posicion
        self.orientacion = orientacion
        self.color = color

    def avanzar(self, matriz):
        color_casilla = matriz.obt_color_casilla(self.posicion)

        if color_casilla == 0:
            matriz.est_color_casilla(self.posicion, 1)
        else:
            matriz.est_color_casilla(self.posicion, 0)

        self.orientacion = act_orientacion(color_casilla, self.orientacion)
        self.posicion = act_posicion(self.orientacion, self.posicion, matriz)


def act_orientacion(color_casilla, orientacion):
    if color_casilla == 0:
        return (orientacion - 1) % 4
    else:
        return (orientacion + 1) % 4


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def act_posicion(orientacion, posicion, matriz):
    x, y = posicion
    return ((x + dx[orientacion]) % matriz.ancho, (y + dy[orientacion]) % matriz.altura)
