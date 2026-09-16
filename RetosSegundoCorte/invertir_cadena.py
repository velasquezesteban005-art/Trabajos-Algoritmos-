def invertir_cadena(cadena: str) -> str:
    # Caso base: cadena vacía o de un solo carácter
    if len(cadena) <= 1:
        return cadena
    
    # Caso recursivo: último carácter + inversión del resto
    return cadena[-1] + invertir_cadena(cadena[:-1])

# Ejemplo
texto = "mañana"
print(invertir_cadena(texto))  # Output: "anañam"