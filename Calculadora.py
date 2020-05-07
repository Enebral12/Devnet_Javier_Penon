#! /usr/bin/env python
# AUTOR: FRANCISCO JAVIER PENON CAMARA 
# CURSO: Becas Digitaliza: DevNet - Ene 20
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
while True:  

    print("\n""\n""MENU CALCULADORA \n"
      "Seleccione operación \n"  
        "1. suma\n" 
        "2. resta\n" 
        "3. multiplicación\n"  
        "4. división\n"
        "5. potencia\n"
        "6. raiz cuadrada\n"
        "7. EXIT")



# Take input from the user  
    select = input("Select operations form 1, 2, 3, 4, 5, 6, 7 :")
    if select == '7':
      break
    
    number_1 = int(input("Enter first number: ")) 
    
      
    if select == '1': 
        number_2 = int(input("Enter second number: "))
        print(number_1, "+", number_2, "=", 
                        suma(number_1, number_2)) 
      
    elif select == '2': 
        number_2 = int(input("Enter second number: "))
        print(number_1, "-", number_2, "=", 
                        resta(number_1, number_2)) 
      
    elif select == '3': 
        number_2 = int(input("Enter second number: "))
        print(number_1, "*", number_2, "=", 
                        multiplicación(number_1, number_2)) 
      
    elif select == '4': 
        number_2 = int(input("Enter second number: "))
        print(number_1, "/", number_2, "=", 
                        división(number_1, number_2)) 
    
    elif select == '5': 
        number_2 = int(input("Enter second number: "))
        print(number_1, "**", number_2, "=", 
                        potencia(number_1, number_2)) 
    
    elif select == '6': 
        print("sqrt", number_1, "=", 
                        raiz(number_1)) 
    
    elif select == '7':
        break
    
    else: 
        print("Invalid input")
            
        break
        
        
           

            