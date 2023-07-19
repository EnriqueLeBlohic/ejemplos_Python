# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setti

import random
import time



"""def comprobarContrasenia(password):
    largo = False
    mayus = False
    numer = False
    dot = False

    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus =  True
        if password[i].isnumeric():
            numer = True
    if largo and mayus and numer:
        return True
    else:
        return False


password = input("Ingrese un contraseña: ")
varificacion = comprobarContrasenia(password)
if varificacion:
    print("ES SEGURA")
else:
    print("No es segura")

if __name__ == '__main__':

    comprobarContrasenia(password)"""


"""def calcularIncremento(salario, x):
    nuevoSalario = salario + (salario * (x/100))
    return nuevoSalario
salarioActual = float(input("Ingrese el salario actual: "))
incremento = float(input("Ingrese el porcentaje de incremento: "))
nuevoSalario =  calcularIncremento(salarioActual, incremento)
print("El nuevo salario del trabajador es: ", nuevoSalario)"""

"""def suma (a,b):
   return a + b
def resta (a,b):
   return a - b
def multiplicación(a,b):
    return a * b
def division(a, b):
    return a/b
def exponenciacion(a, b):
    return a ** b
def radicacion(a, b):
    return a ** (1/b)

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segunfo numero: "))
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Exponenciación")
print("6. Radiación")
opc = int(input("Ingrese la opcion que desea: "))

if opc == 1:
    print(n1,"+",n2, "=",suma(n1,n2))
elif opc == 2:
    print(n1, "-", n2, "=", resta(n1, n2))
elif opc == 3:
    print(n1, "*", n2, "=", multiplicación(n1, n2))
elif opc == 4:
    print(n1, "/", n2, "=", division(n1, n2))
elif opc == 5:
    print(n1, "^", n2, "=", exponenciacion(n1, n2))
elif opc == 6:
    print(n1, "^1/", n2, "=", radicacion(n1, n2))
else:
    print("Error no es una opción")"""

"""def calcularSegundos(dias, horas, minutos, segundos):
    segundosTotales = 0
    segundosTotales += segundos
    segundosTotales += minutos * 60
    segundosTotales += horas * 60 * 60
    segundosTotales += dias * 24 * 60 * 60
    return segundosTotales

dias = int(input("Ingrese la cantidad de días: "))
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))
segundosTotales = calcularSegundos(dias, horas, minutos, segundos)
print("La cantidad de seguntos en el tiempo ingresado es de: ", segundos)"""

"""def calcularIMC(p, a):
    return p / (a*a)

def nivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo Peso"
    elif 18.5 <= IMC <= 24.9:
        return "Normal"
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC <= 34.9:
        return "Obesidad I"
    elif 35 <= IMC <= 39.9:
        return "Obesidad II"
    elif 40 <= IMC <= 49.9:
        return "Obesidad III"
    elif IMC >= 50:
        return "Obesidad IV"

peso = float(input("ingrese el peso (kg): "))
altura = float(input("ingrese la altura (m): "))
print("su nivel de peso es: ", nivelDePeso(calcularIMC(peso, altura)))"""

"""def sum(lista):
    result = 0
    for n in lista:
        result = result + (n)

    print(result)
sum([1,2,3])

def mult(lista):
    result = lista[0]
    i = 1
    while i in range(1,len(lista)):
        result = result * lista[i]
        i +=1
        print(result)
mult([5,5,5])"""

"""def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
    print(nueva_cadena)
inversa("pepito")"""
"""divisas = {
    'Euro': 'E',
    'Dollar': '$',
    'Yen':'Y'
}
divisa = input("escribe una divisa: ")

if divisas.get(divisa):
    print(divisas.get(divisa))
else:
    print("La divisa no se encuentra")"""

"""def countSubarrays(numbers, k):
    # Write your code here
    result = 0
    j = 0
    while j < len(numbers):
        produc_so_far = 1
        for i in range (j + 1, len(numbers)):
            produc_so_far *= numbers[i]
        if produc_so_far <= k:
            result +=1
        if produc_so_far > k:
            j = i + 1
    return result"""

"""----------------BUSQUEDA BINARIA-------------------"""

def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista)-1

    if limite_superior < limite_inferior:
        return -1

    punto_Medio = (limite_inferior + limite_superior) // 2

    if lista[punto_Medio] == objetivo:
        return punto_Medio
    elif objetivo < lista[punto_Medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_Medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_Medio+1, limite_superior)

if __name__=='__main__':

    "mi_lista = [1, 3, 5, 10, 12]"
    "print(busqueda_binaria(mi_lista, 7))"

    # Crear una lista ordenada cn 10000 numeros aleatorios
    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de busqueda ingenua.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"tiempo de busqueda ingenua: {fin - inicio} segundos.")

    # Medir el tiempo de busqueda Binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"tiempo de busqueda Binaria: {fin - inicio} segundos.")