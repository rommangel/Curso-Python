
"""
# if and else
num = int(input('Ingrese un número: '))

if num != 0:
    if num > 0:
        if num % 2 == 0:
            print(f'El número {num} es par positivo')
        else:
            print(f'El número {num} es impar positivo')
    else:
        if num % 2 == 0:
            print(f'El número {num} es par negativo')
        else:
            print(f'El número {num} es impar negativo')
else: 
    print(f'El numero {num} es neutro')
"""

""""
#Elif ingresa una letra 
vocal = input('Ingresa una letra: ')

if vocal == 'a':
    print(vocal, 'Es vocal')
elif vocal == 'e':
    print(vocal, 'Es vocal')
elif vocal == 'i':
    print(vocal, 'Es vocal')
elif vocal == 'o':
    print(vocal, 'Es vocal')
elif vocal == 'u':
    print(vocal, 'Es vocal')
else:
    print(vocal, 'No es vocal')
    
"""
"""
#While
num = int(input('Ingresa un número: '))
cont = 1
suma = 0
while cont <= num:
    suma += cont 
    cont += 14
print (suma)
"""
"""
#Mostrar el numero menor de los  umeros ingresados con while 

n = int(input('Cantidad de números'))
menor = 0
i = 1 
while (i <= n):
    numero = int(input('Número: '))
    if (i == 1):
        menor = numero 
    elif numero < menor:
        menor = numero 
    i += 1

print(f'El número menor es: {menor}')
"""
"""
#For 
palabras = ['Gato', 'León', 'Avión', 'Auto']
for p in palabras:
    print(p, len(p))
    
for i in range(5):
    print(i)
"""
