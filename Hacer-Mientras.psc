Algoritmo RestarHastaCero_Mientras
	// ------------------------------------------
	// TAREA: Restar 1 hasta llegar a 0
	// ESTRUCTURA: Hacer-Mientras (Mientras-Hacer)
	// DOCUMENTACIÓN: El programa recibe un entero 
	// y descuenta una unidad en cada iteración.
	// ------------------------------------------
	
	Definir n Como Entero
	
	Escribir "Ingresa un número para iniciar la cuenta regresiva:"
	Leer n
	
	// El ciclo se ejecuta MIENTRAS n no sea menor a 0
	Mientras n >= 0 Hacer
		Escribir "Valor actual: ", n
		n <- n - 1 // Decremento de 1
	FinMientras
	
	Escribir "Proceso terminado. Llegaste a cero."
FinAlgoritmo