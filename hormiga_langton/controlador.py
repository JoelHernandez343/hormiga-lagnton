from .hormiga import Hormiga
from .matriz import Matriz


class Controlador:
    def __init__(self, dimensiones, dict_hormigas):
        ancho, altura = dimensiones
        self.matriz = Matriz(ancho, altura)

        self.hormigas = []
        for h in dict_hormigas:

            color = h["color"]
            orientacion = h["orientacion"]
            x = h["posicion"]["x"]
            y = h["posicion"]["y"]

            self.hormigas.append(Hormiga((x, y), orientacion, color))

    def paso(self):
        for hormiga in self.hormigas:
            hormiga.avanzar(self.matriz)

    def show_console(self):
        for y in range(self.matriz.altura):
            for x in range(self.matriz.ancho):
                print(f"{self.matriz.matriz[y][x]}", end="")

                flag = False

                for hormiga in self.hormigas:
                    xh, yh = hormiga.posicion
                    if xh == x and yh == y:
                        flag = True
                        print(f"({hormiga.color},{hormiga.orientacion})", end="")
                        break

                if not flag:
                    print("     ", end="")

            print()
