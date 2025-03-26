#EXercicio 4:
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
            if nodo.esquerdo:
                self._inserir(nodo.esquerdo, valor)
            else:
                nodo.esquerdo = Nodo(valor)
        else:
            if nodo.direito:
                self._inserir(nodo.direito, valor)
            else:
                nodo.direito = Nodo(valor)

arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
