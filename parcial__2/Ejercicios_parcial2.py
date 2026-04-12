# Ejercicio 1
print("--- Ejercicio 1 ---")
palabra = " elefante "
palabra_limpia = palabra.strip()
print(palabra_limpia)
print(palabra_limpia.count("e"))

# Ejercicio 2
print("\n--- Ejercicio 2 ---")
texto2 = "Angel Anzora"
texto2_titulo = texto2.title()
print(texto2_titulo.replace("Angel", "Anzora"))

# Ejercicio 3
print("\n--- Ejercicio 3 ---")
texto3 = "ING. Anzora"
texto3_sin_prefijo = texto3.removeprefix("ING. ")
print(texto3_sin_prefijo.upper())

# Ejercicio 4
print("\n--- Ejercicio 4 ---")
texto4 = "CANTANDO"
texto4_minusculas = texto4.lower()
texto4_sin_sufijo = texto4_minusculas.removesuffix("ando")
print(texto4_sin_sufijo)
print(texto4_sin_sufijo.find("t"))

# Ejercicio 5
print("\n--- Ejercicio 5 ---")
texto5 = "pYTHON"
texto5_invertido = texto5.swapcase()
print(texto5_invertido.ljust(15, "*"))

# Ejercicio 6
print("\n--- Ejercicio 6 ---")
texto6 = "Angel"
texto6_normalizado = texto6.casefold()
texto6_sin_espacios = texto6_normalizado.replace(" ", "")
print(texto6_normalizado)
print(texto6_sin_espacios.isalpha())

# Ejercicio 7
print("\n--- Ejercicio 7 ---")
texto7 = "42"
texto7_relleno = texto7.zfill(5)
print(texto7_relleno)
print(texto7_relleno.endswith("2"))

# Ejercicio 8
print("\n--- Ejercicio 8 ---")
texto8 = """Linea uno
Linea dos
Linea tres"""
print(texto8.count("a"))
print(texto8.splitlines())

# Ejercicio 9
print("\n--- Ejercicio 9 ---")
texto9 = "Any time y Anytime"
texto9_reemplazado = texto9.replace("Any time", "Always")
print(texto9_reemplazado.upper())

# Ejercicio 10
print("\n--- Ejercicio 10 ---")
texto10 = "Python2026"
es_alfanumerico = texto10.isalnum()
print(es_alfanumerico)
if es_alfanumerico:
    texto10_min = texto10.lower()
    print(texto10_min.replace("2026", ""))

# Ejercicio 11
print("\n--- Ejercicio 11 ---")
texto11 = " el nido matinal "
texto11_limpio = texto11.strip().title()
print(texto11_limpio.center(30, "-"))

# Ejercicio 12
print("\n--- Ejercicio 12 ---")
texto12 = "ING. Angel.txt"
texto12_sin_sufijo = texto12.removesuffix(".txt")
texto12_sin_prefijo = texto12_sin_sufijo.removeprefix("ING. ")
texto12_min = texto12_sin_prefijo.lower()
print(texto12_min.split())

cd parcial 2