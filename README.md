Tarea de PSeint.

##  Descripción
Este repositorio contiene un algoritmo creado apartir de la enseñanza y paciencia,
el programa solicita un número inicial al usuario y realiza una cuenta regresiva
restando de 1 en 1 hasta llegar a 0 según las indicaciones del Ing. Alfredo Sorto.

##  Estructura Utilizada
Para lograr la repetición (iteración), se utilizó la estructura de control 
**Mientras-Hacer** ("Mientras <condición> Hacer").

##  Codigo de PSeint:

Algoritmo Laboratorio_Angel_Anzora
    Definir numero_original, contador Como Entero
    Definir mitad_exacta Como Real
    Definir sigue_restando Como Logico
    
    Escribir "Introduce un número para iniciar la cuenta atrás hasta 0:"
    Leer numero_original
    
    Si No (numero_original > 0) Entonces
        Escribir "Error: El número debe ser mayor a cero."
    Sino
        contador <- numero_original 
        sigue_restando <- Verdadero
        
        Escribir "--- Iniciando proceso ---"
        
        Repetir
            Escribir "Valor actual: ", contador
            
            Si contador <= 3 Y contador > 0 Entonces
                Escribir "Falta poco para el final..."
            FinSi
            
            contador <- contador - 1
            
            Si contador < 0 Entonces
                sigue_restando <- Falso
            FinSi
            
        Hasta Que contador < 0 O sigue_restando = Falso
        
        Escribir "--- ¡Llegamos a 0 con éxito! ---"
        
        mitad_exacta <- numero_original / 2 
        Escribir "La mitad de tu número original (", numero_original, ") es: ", mitad_exacta
        
    FinSi
FinAlgoritmo

##  Explicación del código
​
Utilice nombres descriptivos y coherentes para identificar fácilmente la función de cada variable:  

​numero_original y contador (Entero): Almacenan el número ingresado por el usuario y el valor temporal que irá restando de 1 en 1, en ese mismo orden.  

​mitad_exacta (Real): Se utiliza al final del programa para almacenar y mostrar el resultado de una división, permitiendo trabajar con decimales.  

​sigue_restando (Lógico): Controla el estado del programa mediante los valores booleanos Verdadero y Falso.

##  Entrada y validación de datos

El programa solicita un número inicial utilizando la instrucción Leer.  
​Se aplica una condición inicial con el operador lógico NO (Si No (numero_original > 0)) para garantizar que el usuario ingrese un número estrictamente positivo.

##  Operadores lógicos

Decidi integrar dentro de la algoritmica logica los siguientes operadores:  
​
Operador Y: Utilizado en una condición interna (Si contador <= 3 Y contador > 0) para imprimir un mensaje de aviso cuando la cuenta regresiva está por terminar.

​Operador O: Empleado en la condición de salida del ciclo (Hasta Que contador < 0 O sigue_restando = Falso), asegurando que el ciclo se rompa ya sea por llegar al límite numérico o porque la variable lógica cambió su estado.

-------------------
**Autor:** Angel Josue Hernandez Anzora
**Materia:** Fundamentos de Programación Deidad
