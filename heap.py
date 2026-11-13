"""Fila de Prioridades — Min-Heap (árvore binária quase completa)."""


class FilaPrioridade:
    """
    Min-Heap armazenado em lista. Por ser uma árvore binária QUASE COMPLETA,
    não precisa de ponteiros:
        pai(i)       = (i - 1) // 2
        filho_esq(i) = 2*i + 1
        filho_dir(i) = 2*i + 2
    Menor número = maior prioridade.
    """

    def __init__(self):
        self.heap = [] 

    def __len__(self):
        return len(self.heap)

    def inserir(self, prioridade, item):
        self.heap.append((prioridade, item))
        self._subir(len(self.heap) - 1)

    def remover(self):
        if not self.heap:
            raise IndexError("Fila vazia")
        topo = self.heap[0]
        ultimo = self.heap.pop()
        if self.heap:
            self.heap[0] = ultimo
            self._descer(0)
        return topo

    def espiar(self):
        return self.heap[0] if self.heap else None

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self.heap[i][0] < self.heap[pai][0]:
                self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self.heap)
        while True:
            menor = i
            esq, dir_ = 2 * i + 1, 2 * i + 2
            if esq < n and self.heap[esq][0] < self.heap[menor][0]:
                menor = esq
            if dir_ < n and self.heap[dir_][0] < self.heap[menor][0]:
                menor = dir_
            if menor == i:
                break
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            i = menor