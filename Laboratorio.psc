Algoritmo Laboratorio
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