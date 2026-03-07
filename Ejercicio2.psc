
	Algoritmo Ejercicio2
		Definir num, suma Como Real
		suma <- 0
		Repetir
			Escribir "Ingrese un número (negativo para salir):"
			Leer num
			Si num >= 0 Entonces
				suma <- suma + num
			FinSi
		Hasta Que num < 0
		Escribir "La suma de los números positivos es: ", suma
FinAlgoritmo