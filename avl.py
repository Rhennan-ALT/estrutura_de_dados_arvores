"""Árvore AVL — balanceamento automático por altura."""


class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.altura = 1


class ArvoreAVL:
    """Para todo nó, |altura(esq) - altura(dir)| <= 1."""

    def __init__(self):
        self.raiz = None

    @staticmethod
    def _altura(no):
        return no.altura if no else 0

    def _fator(self, no):
        return self._altura(no.esq) - self._altura(no.dir) if no else 0

    def _atualizar(self, no):
        no.altura = 1 + max(self._altura(no.esq), self._altura(no.dir))

    def _rot_dir(self, y):
        x = y.esq
        y.esq = x.dir
        x.dir = y
        self._atualizar(y)
        self._atualizar(x)
        return x

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq
        y.esq = x
        self._atualizar(x)
        self._atualizar(y)
        return y

    def _balancear(self, no):
        self._atualizar(no)
        fb = self._fator(no)
        if fb > 1:                                  
            if self._fator(no.esq) < 0:             
                no.esq = self._rot_esq(no.esq)
            return self._rot_dir(no)
        if fb < -1:                                 
            if self._fator(no.dir) > 0:             
                no.dir = self._rot_dir(no.dir)
            return self._rot_esq(no)
        return no

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return NoAVL(chave)
        if chave < no.chave:
            no.esq = self._inserir(no.esq, chave)
        elif chave > no.chave:
            no.dir = self._inserir(no.dir, chave)
        else:
            return no  # (sem duplicatas)
        return self._balancear(no)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return None
        if chave < no.chave:
            no.esq = self._remover(no.esq, chave)
        elif chave > no.chave:
            no.dir = self._remover(no.dir, chave)
        else:
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            suc = no.dir
            while suc.esq:
                suc = suc.esq
            no.chave = suc.chave
            no.dir = self._remover(no.dir, suc.chave)
        return self._balancear(no)

    def buscar(self, chave):
        no = self.raiz
        while no:
            if chave == no.chave:
                return True
            no = no.esq if chave < no.chave else no.dir
        return False

    def em_ordem(self):
        resultado = []

        def visitar(no):
            if no:
                visitar(no.esq)
                resultado.append(no.chave)
                visitar(no.dir)

        visitar(self.raiz)
        return resultado