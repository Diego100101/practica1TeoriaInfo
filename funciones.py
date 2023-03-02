#------------------------------------------------------------------------------
# Universidad Autónoma Metropolitana: unidad Lerma
# Programador: Diego Cantoral González
# UEA: Teoría de la información y la codificación
# 1 de marzo de 2023
#------------------------------------------------------------------------------

# Este es un código complementario a los códigos 'textoUsuario.py' y 'textoNoUsuario.py', aquí se
# codificaron todos los algoritmos que expresan las ecuaciones para la probabilidad y entropía,
# de primer, segundo y tercer orden. También se codificó una función para normalizar las letras
# del archivo de texto y del caracter ingresado.

import math

# Se normalizan las letras reemplazando la letra con tilde, diéresis, etc, por la letra normal
def normalizar(string):
    string = string.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')\
        .replace('à','a').replace('è','e').replace('ì','i').replace('ò','o').replace('ù','u').replace('ü','u').replace('ö','o')\
        .replace('ï','i').replace('ë','e').replace('â','a').replace('ê','e').replace('î','i').replace('ô','o').replace('û','u')
    return string

# Probabilidad
# Se calcula la probabilidad con: P(x) = número de veces que aparece la letra/total de caracteres
def probabilidad( cuentaLetra, total):
    prob = cuentaLetra/total
    return prob

# Entropía
# Se calcula la entropía con: H(x) = P(x)log_2(1/P(x))
def entropia(probabilidad):
    if probabilidad == 0:
        print("División con cero")
    else:
        x = 1 / probabilidad
        H_x = probabilidad * math.log( x, 2)
    return H_x
# Entropía segundo orden
# Se calcula la entropía de segundo orden con: H(x²) = 2H(x)
def entropiaOrdenDos(entropia):
    H_x2 = 2 * entropia
    return H_x2

# Entropía tercer orden
# Se calcula la entropía de tercer orden con: H(x³) = 3H(x)
def entropiaOrdenTres(entropia):
    H_x3 = 3 * entropia
    return H_x3