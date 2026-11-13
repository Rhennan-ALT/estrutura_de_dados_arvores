import matplotlib.pyplot as plt

from heap import FilaPrioridade
from avl import ArvoreAVL
from rubro_negra import ArvoreRubroNegra
from visualizacao import desenhar_heap, desenhar_avl, desenhar_rubro_negra


def exemplo_heap():
    fila = FilaPrioridade()
    for prioridade, tarefa in [(3, "Enviar relatório"), (1, "Atender emergência"),
                               (4, "Organizar arquivos"), (2, "Responder e-mails"),
                               (5, "Tomar café"), (7, "Almoçar"), (6, "Reunião")]:
        fila.inserir(prioridade, tarefa)
    print("HEAP -> array interno:", [p for p, _ in fila.heap])
    return fila


def exemplo_avl():
    avl = ArvoreAVL()
    for valor in [10, 20, 30, 40, 50, 25]: 
        avl.inserir(valor)
    print("AVL  -> em ordem:", avl.em_ordem(), "| altura da raiz:", avl.raiz.altura)
    return avl


def exemplo_rubro_negra():
    rn = ArvoreRubroNegra()
    for valor in [10, 20, 30, 15, 25, 5, 1]:
        rn.inserir(valor)
    print("RN   -> em ordem:", rn.em_ordem(), "| altura negra:", rn.altura_negra())
    return rn


def main():
    fila = exemplo_heap()
    avl = exemplo_avl()
    rn = exemplo_rubro_negra()

    fig, eixos = plt.subplots(1, 3, figsize=(18, 6))
    desenhar_heap(eixos[0], fila)
    desenhar_avl(eixos[1], avl)
    desenhar_rubro_negra(eixos[2], rn)
    fig.suptitle("Exemplos de Árvores", fontsize=16)
    fig.tight_layout()

    fig.savefig("arvores.png", dpi=120)
    print("Imagem salva em arvores.png")
    plt.show()


if __name__ == "__main__":
    main()