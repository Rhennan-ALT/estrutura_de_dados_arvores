"""Árvore Rubro-Negra — balanceamento por cores."""

VERMELHO, PRETO = True, False


class NoRN:
    def __init__(self, chave, cor=VERMELHO, nil=None):
        self.chave = chave
        self.cor = cor
        self.esq = nil
        self.dir = nil
        self.pai = nil


class ArvoreRubroNegra:
    """
    Propriedades:
      1. Todo nó é vermelho ou preto.
      2. A raiz é preta.
      3. Todas as folhas (NIL) são pretas.
      4. Filho de nó vermelho é preto (sem dois vermelhos seguidos).
      5. Todo caminho de um nó até suas folhas tem o mesmo nº de nós pretos.
    """

    def __init__(self):
        self.NIL = NoRN(None, PRETO)
        self.raiz = self.NIL

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq
        if y.esq != self.NIL:
            y.esq.pai = x
        y.pai = x.pai
        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y

    def _rot_dir(self, x):
        y = x.esq
        x.esq = y.dir
        if y.dir != self.NIL:
            y.dir.pai = x
        y.pai = x.pai
        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.dir:
            x.pai.dir = y
        else:
            x.pai.esq = y
        y.dir = x
        x.pai = y

    def inserir(self, chave):
        z = NoRN(chave, VERMELHO, self.NIL)
        y, x = self.NIL, self.raiz
        while x != self.NIL:
            y = x
            if chave == x.chave:
                return  # sem duplicatas
            x = x.esq if chave < x.chave else x.dir
        z.pai = y
        if y == self.NIL:
            self.raiz = z
        elif chave < y.chave:
            y.esq = z
        else:
            y.dir = z
        self._corrigir_insercao(z)

    def _corrigir_insercao(self, z):
        while z.pai.cor == VERMELHO:
            if z.pai == z.pai.pai.esq:
                tio = z.pai.pai.dir
                if tio.cor == VERMELHO:                 # (caso 1: recolorir)
                    z.pai.cor = PRETO
                    tio.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    z = z.pai.pai
                else:
                    if z == z.pai.dir:                  # (caso 2: rotação dupla)
                        z = z.pai
                        self._rot_esq(z)
                    z.pai.cor = PRETO                  
                    z.pai.pai.cor = VERMELHO
                    self._rot_dir(z.pai.pai)
            else:
                tio = z.pai.pai.esq
                if tio.cor == VERMELHO:
                    z.pai.cor = PRETO
                    tio.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    z = z.pai.pai
                else:
                    if z == z.pai.esq:
                        z = z.pai
                        self._rot_dir(z)
                    z.pai.cor = PRETO
                    z.pai.pai.cor = VERMELHO
                    self._rot_esq(z.pai.pai)
        self.raiz.cor = PRETO                       # (seguindo o mesmo exemplo mostrado em sala)

    def buscar(self, chave):
        no = self.raiz
        while no != self.NIL:
            if chave == no.chave:
                return True
            no = no.esq if chave < no.chave else no.dir
        return False

    def em_ordem(self):
        resultado = []

        def visitar(no):
            if no != self.NIL:
                visitar(no.esq)
                resultado.append(no.chave)
                visitar(no.dir)

        visitar(self.raiz)
        return resultado

    def altura_negra(self):
        h, no = 0, self.raiz
        while no != self.NIL:
            if no.cor == PRETO:
                h += 1
            no = no.esq
        return h