#------------------------------------------------------------------------------
# Universidad Autónoma Metropolitana: unidad Lerma
# Programador: Diego Cantoral González
# UEA: Teoría de la información y la codificación
# 1 de marzo de 2023
#------------------------------------------------------------------------------

# Este es un código alternativo al código 'textoUsuario.py', a diferencia, únicamente permite ingresar
# la ruta del archivo de texto, pero imprime las probabilidades, entropías y veces que aparece en el
# archivo de todas las letras del alfabeto establecido.
import funciones

txt = input("Ingrese el libro en formato .txt, o su ruta absoluta\n")

# Se abre el archivo con extensión ".txt" y se asigna a una variable llamada 'libro' para ser leído
# Después, con la variable 'contenido', leemos los caracteres de 'libro' y cambiamos a mínusculas y quitamos acentos.
with open(txt, encoding="utf-8") as libro:
    contenido = libro.read()
    contenido = funciones.normalizar(contenido)

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

# Se imprimen la cuenta de los caracteres totales en el archivo
print(f"Caracteres totales en el texto: {caracteres}\n")

# Se utiliza un ciclo 'for' para calcular las probabilidades y entropías de cada letra del alfabeto
for a in alfabeto:
    # Se obtiene la cuenta total de la letra en el archivo
    letraContar = contenido.count(a)

    # Se verifica que el valor anterior no sea cero, pues podría ocasionar una división por cero en la entropía
    if letraContar == 0:
        print(f"No existe <{a}> en el texto.\n")
    else:
        # Se calcula e imprime la probabilidad y entropía
        probabilidadLetra = funciones.probabilidad(letraContar, caracteres)
        entropiaLetra = funciones.entropia(probabilidadLetra)
        entropiaDos = funciones.entropiaOrdenDos(entropiaLetra)
        entropiaTres = funciones.entropiaOrdenTres(entropiaLetra)
        print(f"Número de <{a}> dentro del texto: {letraContar}")
        print(f"Probabilidad de la letra o combinación en el texto: P(x) = {probabilidadLetra:.5f} "
              f"= {probabilidadLetra * 100:.4f}%")
        print(f"Entropía: H(x) = {entropiaLetra:.4f}")
        print(f"Entropía de orden dos: H(x2) = {entropiaDos:.4f}")
        print(f"Entropía de orden tres: H(x3) = {entropiaTres:.4f}\n")

