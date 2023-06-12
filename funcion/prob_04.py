def es_vocal(caracter):
    vocales = "aeiou"
    if caracter.lower() in vocales:
        return True
    else:
        return False
    
caracter = "A"
print(es_vocal(caracter))
