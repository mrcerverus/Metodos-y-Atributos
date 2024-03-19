from pizza import Pizza

""" 
a. valor de atributos de clase
"""
tamaño, precio = Pizza.tamano , Pizza.precio
print(f"El tamño de la pizza es: {tamaño} y su precio es: ${precio}")

""" 
b. usar metodo Pizza.validar()
"""
texto = 'Salsa de tomate'
lista = ['Salsa de tomate' , 'Salsa Bbq']
test = Pizza.validar( texto , lista )
if test == True:
    print(f"Ingrediente, {texto} dentro de lista de ingredientes")
else:
    print("Ingrediente no válido")

""" 
c. Solicitar ingredientes y tipo de masa al usuario
"""
partida = Pizza() #instanciar
pedido = partida.realizar_pedido() #metodo de instancia

"""
d. Imprimir en pantalla elección del usuario
"""
print(f'''
Su pedido es el siguiente:
Proteina: {partida.ingrediente_proteico}
Vegetales: {partida.ingrediente_vegetal1}, {partida.ingrediente_vegetal2}
El tipo de masa es: {partida.tipo_masa}
''')

""" 
e. Pedido de pizza válido o no?
"""
if partida.es_valida == True:
    print("Su pedido es válido")
else:
    print("Su pedido no es válido")