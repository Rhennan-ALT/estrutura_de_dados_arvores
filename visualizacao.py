"""Funções para desenhar as árvores usando matplotlib."""

from rubro_negra import VERMELHO


def _posicoes(raiz, filhos):
    """Calcula (x, y) de cada nó: x pela ordem in-order, y pela profundidade."""
    pos = {}
    contador = [0]

    def visitar(no, profundidade):
        esq, dir_ = filhos(no)
        if esq is not None:
            visitar(esq, profundidade + 1)
        pos[no] = (contador[0], -profundidade)
        contador[0] += 1
        if dir_ is not None:
            visitar(dir_, profundidade + 1)

    visitar(raiz, 0)
    return pos


def _desenhar(ax, raiz, filhos, rotulo, cor, titulo):
    """Desenho genérico: serve para qualquer árvore binária."""
    ax.set_title(titulo, fontsize=13, fontweight="bold")
    ax.axis("off")
    if raiz is None:
        ax.text(0.5, 0.5, "(vazia)", ha="center", transform=ax.transAxes)
        return

    pos = _posicoes(raiz, filhos)

    # arestas
    for no, (x, y) in pos.items():
        for filho in filhos(no):
            if filho is not None:
                fx, fy = pos[filho]
                ax.plot([x, fx], [y, fy], color="#888888", zorder=1)

    # nós
    for no, (x, y) in pos.items():
        fundo, texto = cor(no)
        ax.scatter(x, y, s=1100, c=fundo, edgecolors="black", zorder=2)
        ax.text(x, y, rotulo(no), ha="center", va="center",
                color=texto, fontsize=9, fontweight="bold", zorder=3)

    ax.margins(0.12)


def desenhar_heap(ax, fila):
    n = len(fila.heap)
    raiz = 0 if n else None

    def filhos(i):
        esq, dir_ = 2 * i + 1, 2 * i + 2
        return (esq if esq < n else None, dir_ if dir_ < n else None)

    _desenhar(
        ax, raiz, filhos,
        rotulo=lambda i: f"{fila.heap[i][0]}",
        cor=lambda i: ("#4C9BE8", "white"),
        titulo="Heap (fila de prioridades)",
    )


def desenhar_avl(ax, arvore):
    _desenhar(
        ax, arvore.raiz,
        filhos=lambda no: (no.esq, no.dir),
        rotulo=lambda no: f"{no.chave}\nh={no.altura}",
        cor=lambda no: ("#3DAA6D", "white"),
        titulo="Árvore AVL",
    )


def desenhar_rubro_negra(ax, arvore):
    nil = arvore.NIL
    raiz = None if arvore.raiz == nil else arvore.raiz

    def filhos(no):
        return (None if no.esq == nil else no.esq,
                None if no.dir == nil else no.dir)

    _desenhar(
        ax, raiz, filhos,
        rotulo=lambda no: f"{no.chave}",
        cor=lambda no: ("#D62828", "white") if no.cor == VERMELHO else ("#1A1A1A", "white"),
        titulo="Árvore Rubro-Negra",
    )