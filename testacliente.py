original = 'Olá, mundo'
encodado = original.encode('utf-8')
decodado = encodado.decode('utf-8') # Funciona perfeitamente!

print("\n\n")
print(encodado)
print(decodado)
print(original == decodado)