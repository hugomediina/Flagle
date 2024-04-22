import os
import random
import json

from PIL import Image
from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

Colores = [(int, int, int)]
with open('../lib/codes.json', 'r', encoding='utf-8') as f:
    paises_data = json.load(f)

NOMBRES_PAISES = list(paises_data.values())
PAISES = [pais[:-len(".jpg")] for pais in os.listdir("../img/original_flags")]


class GestionBanderas:
    def __init__(self):
        self.guess = None
        self.actual = None
        self.pais_a_adivinar = None
        self.tolerancia = 45

    def escoger_pais(self):
        self.pais_a_adivinar = random.choice(PAISES)
        self.guess = crear_matriz_colores(self.pais_a_adivinar)

    def actualizar_imagen(self, intento):
        pais_intento = crear_matriz_colores(intento)
        if self.actual is None:
            self.actual = union_banderas(self.guess, pais_intento)
        else:
            self.actual = suma_de_matrices(self.actual, union_banderas(self.guess, pais_intento))
        imagen = matriz_a_bandera(self.actual)
        pais_intento_img = matriz_a_bandera(pais_intento)
        imagen.save("static/bandera.jpg")
        pais_intento_img.save("static/last_try.jpg")

    def actualizar_tolerancia(self, nueva_tolerancia):
        self.tolerancia = nueva_tolerancia


def set_imagen_black():
    Image.new('RGB', (640, 488)).save('static/bandera.jpg')
    Image.new('RGB', (640, 488)).save('static/last_try.jpg')


def crear_matriz_colores(pais: str) -> Colores:
    i = Image.open("../img/all_flags/" + pais + ".jpg", 'r')
    imagen_rgb = i.convert('RGB')
    ancho, alto = imagen_rgb.size

    matriz_bandera = []

    for y in range(alto):
        fila = []
        for x in range(ancho):
            color = imagen_rgb.getpixel((x, y))
            fila.append(color)
        matriz_bandera.append(fila)
    return matriz_bandera


def matriz_a_bandera(matriz: Colores):
    ancho = len(matriz[0])
    alto = len(matriz)

    imagen = Image.new('RGB', (ancho, alto))

    for y in range(alto):
        for x in range(ancho):
            color = matriz[y][x]
            imagen.putpixel((x, y), color)

    return imagen


def union_banderas(matriz_inicio: Colores, matriz_guess: Colores) -> Colores:
    def colores_similares(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2

        distancia_color = ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5
        return distancia_color <= manager.tolerancia

    alto1, ancho1 = len(matriz_inicio), len(matriz_inicio[0])
    alto2, ancho2 = len(matriz_guess), len(matriz_guess[0])
    alto_nuevo = max(alto1, alto2)
    ancho_nuevo = max(ancho1, ancho2)

    matriz_nueva = [[(0, 0, 0)] * ancho_nuevo for _ in range(alto_nuevo)]

    for y in range(alto_nuevo):
        for x in range(ancho_nuevo):
            color1 = (0, 0, 0)
            color2 = (0, 0, 0)

            if 0 <= y < alto1 and 0 <= x < ancho1:
                color1 = matriz_inicio[y][x]
            if 0 <= y < alto2 and 0 <= x < ancho2:
                color2 = matriz_guess[y][x]
            if colores_similares(color1, color2):
                matriz_nueva[y][x] = color1
    return matriz_nueva


def suma_de_matrices(actual: Colores, guess: Colores):
    suma_matriz = actual
    alto, ancho = len(suma_matriz), len(suma_matriz[0])

    alto_guess, ancho_guess = len(guess), len(guess[0])

    for y in range(min(alto, alto_guess)):
        for x in range(min(ancho, ancho_guess)):
            color2 = guess[y][x]
            if color2 != (0, 0, 0):
                suma_matriz[y][x] = color2
    return suma_matriz


@app.route('/')
def index():
    return render_template('index.html', pais_adivinar=manager.pais_a_adivinar,
                           paises=NOMBRES_PAISES, tolerancia=manager.tolerancia,
                           lasttry=url_for('static', filename='last_try.jpg'))


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        intento = request.form['nombre_bandera']
        x = None

        if intento != paises_data[manager.pais_a_adivinar]:
            if intento in NOMBRES_PAISES:
                for codigo, nombre in paises_data.items():
                    if nombre == intento:
                        x = codigo
                        break
                manager.actualizar_imagen(x)
            else:
                message = 'El país ingresado no está en la lista.'
                return render_template('index.html', pais_adivinar=manager.pais_a_adivinar,
                                       paises=NOMBRES_PAISES, tolerancia=manager.tolerancia, message=message)
            nueva_tolerancia = int(request.form['tolerancia'])
            manager.actualizar_tolerancia(nueva_tolerancia)
            return redirect(url_for('index'))
        else:
            for codigo, nombre in paises_data.items():
                if nombre == intento:
                    x = codigo
                    break
            manager.actualizar_imagen(x)
            congrats = 'Enhorabuena, has adivinado la bandera: \n '+ paises_data[manager.pais_a_adivinar]
            return render_template('index.html', pais_adivinar=manager.pais_a_adivinar,
                                   paises=NOMBRES_PAISES, tolerancia=manager.tolerancia, congrats=congrats)


if __name__ == '__main__':
    manager = GestionBanderas()
    manager.escoger_pais()
    set_imagen_black()

    print(paises_data[manager.pais_a_adivinar])
    app.run()
