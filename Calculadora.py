#! /usr/bin/env python
# Python programa para calculadora 
import math
  
# Funcion suma de dos números  
def suma(num1, num2): 
    return num1 + num2 
  
# Función resta de dos números 
def resta(num1, num2): 
    return num1 - num2 
  
# Función multiplicación de dos números
def multiplicación(num1, num2): 
    return num1 * num2 
  
# Función división de dos números
def división(num1, num2): 
    return num1 / num2 

# Función para elevar dos números  
def potencia(num1, num2): 
    return num1 ** num2     

# Función raiz cuadrada de un número  
def raiz(num1): 
   return math.sqrt(num1)         
  
print("Seleccione operación -\n"  
        "1. suma\n" 
        "2. resta\n" 
        "3. multiplicación\n"  
        "4. división\n"
        "5. potencia\n"
        "6. raiz cuadrada\n")

  
# Take input from the user  
select = input("Select operations form 1, 2, 3, 4, 5, 6 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", 
                    suma(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", 
                    resta(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", 
                    multiplicación(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", 
                    división(number_1, number_2)) 

elif select == '5': 
    print(number_1, "**", number_2, "=", 
                    potencia(number_1, number_2)) 

elif select == '6': 
    print("sqrt", number_1, "=", 
                    raiz(number_1)) 

else: 
    print("Invalid input")
