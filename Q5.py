#Exercicio 5:
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.esquerdo is None:
                nodo.esquerdo = Nodo(valor)
            else:
                self._inserir(nodo.esquerdo, valor)
        else:
            if nodo.direito is None:
                nodo.direito = Nodo(valor)
            else:
                self._inserir(nodo.direito, valor)

    def imprimir_filhos(self, valor):
        nodo = self._encontrar(self.raiz, valor)
        if nodo:
            if nodo.esquerdo:
                print(nodo.esquerdo.valor)
            if nodo.direito:
                print(nodo.direito.valor)

    def _encontrar(self, nodo, valor):
        if not nodo:
            return None
        if nodo.valor == valor:
            return nodo
        elif valor < nodo.valor:
            return self._encontrar(nodo.esquerdo, valor)
        else:
            return self._encontrar(nodo.direito, valor)

arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)

arvore.imprimir_filhos(10)