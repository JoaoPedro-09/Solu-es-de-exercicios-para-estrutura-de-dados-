#Exercicio 2:

class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, elemento):
        self.fila.append(elemento)

    def desenfileirar(self):
        if self.fila:
            return self.fila.pop(0)
        else:
            return None

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
print(fila.desenfileirar())
