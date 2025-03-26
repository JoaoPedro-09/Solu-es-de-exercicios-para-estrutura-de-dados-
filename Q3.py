#Exercicio 3:

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

    def reverter(self):
        reverso = []
        while self.fila:
            reverso.append(self.desenfileirar())
        return reverso

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(fila.reverter())