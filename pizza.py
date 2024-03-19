from ingredientes import proteina
from ingredientes import vegetal
from ingredientes import masa

class Pizza():
    #atributos de clase
    tamano = 'Familiar'
    precio = 10000
    
    #validar si un elemento esta dentro de la lista
    @staticmethod
    def validar(texto , lista):
        return texto in lista
    
    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False
    
    #ingreso de ingredientes
    
    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico (pollo , vacuno , carne): \n").lower()
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate , aceituna , champinon): \n").lower()
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate , aceituna , champinon): \n").lower()
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional, delgada): \n").lower()

        # Validación de ingredientes y tipo de masa
        self.es_valida = (
            self.validar(self.ingrediente_proteico, proteina)
            and self.validar(self.ingrediente_vegetal1, vegetal)
            and self.validar(self.ingrediente_vegetal2, vegetal)
            and self.validar(self.tipo_masa, masa)
        )




