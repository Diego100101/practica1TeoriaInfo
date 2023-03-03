#------------------------------------------------------------------------------
# Universidad Autónoma Metropolitana: unidad Lerma
# Programador: Diego Cantoral González
# UEA: Teoría de la información y la codificación
# 1 de marzo de 2023
#------------------------------------------------------------------------------

# Este código recibe un archivo de texto (extensión .txt) y un caracter, o combinación de caracteres,
# de interés para que pueda regresar los cálculos de la probabilidad y entropía, así como el número
# de veces que aparece en el texto y los caracteres totales del archivo. Está pensado para que el
# usuario pueda ingresar manualmente el caracter y la ruta del archivo de texto.

import funciones

# Se pide ingresar el archivo con extensión .txt que se desea analizar
txt = input("Ingrese el libro en formato .txt, o su ruta asboluta\n")

# Se abre el archivo con extensión ".txt" y se asigna a una variable llamada 'libro' para ser leído
# Después, con la variable 'contenido', leemos los caracteres de 'libro' y cambiamos a mínusculas y quitamos acentos.
with open(txt, encoding="utf-8") as libro:
    contenido = libro.read()
    contenido = funciones.normalizar(contenido)

# Se solicita ingresar la letra por buscar y se normaliza.
letra = input('Ingresa letra por buscar o combinación: \n')
letra = funciones.normalizar(letra)

# Se crea una lista que contiene un alfabeto con los caracteres de interés para el texto.
alfabeto = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']

# Se toman únicamente los caracteres del contenido con base al alfabeto creado.
# Para ello se itera y se compara
# Se utiliza un contador para llevar la cuenta de los caracteres totales dentro del archivo
caracteres = 0

for a in alfabeto:
    for i in contenido:
        if i == a:
            caracteres += 1

# Cuenta el número de veces que aparece la letra ingresada dentro del texto
cuenta = contenido.count(letra)

# Se asegura que la cuenta no sea cero
# Calcula probabilidad y entropía e imprime los resultados
entropia = 0
if cuenta == 0:
    print("No existe esta combinación en el texto):")
else:
    probabilidadLetra = funciones.probabilidad(cuenta, caracteres)
    entropiaLetra = funciones.entropia(probabilidadLetra)
    entropia = entropia + entropiaLetra
    entropiaDos = funciones.entropiaOrdenDos(entropiaLetra)
    entropiaTres = funciones.entropiaOrdenTres(entropiaLetra)
    informacion = funciones.informacion(probabilidadLetra)
    print(f"Número de <{letra}> dentro del texto: {cuenta}")
    print(f"Caracteres: {caracteres}")
    print(f"Probabilidad de la letra o combinación en el texto: P(x) = {probabilidadLetra:.5f} "
          f"= {probabilidadLetra * 100:.4f}%")
    print(f"Información: I(x) = {informacion:.4f}")
    print(f"Entropía: H(x) = {entropiaLetra:.4f}")
    print(f"Entropía de orden dos: H(x2) = {entropiaDos:.4f}")
    print(f"Entropía de orden tres: H(x3) = {entropiaTres:.4f}")
