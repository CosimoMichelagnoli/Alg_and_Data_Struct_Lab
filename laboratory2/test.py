import ABR
import ARN
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def array(n):
    A = []
    for i in range(0, n):
        A.insert(i, int(np.random.rand() * 100))
    return A


def array_ordinato_al_contrario(n):
    A = array_ordinato(n)
    A.reverse()
    return A


def array_ordinato(n):
    A = []
    for i in range(0, n):
        A.insert(i, i)
    return A


def crea_albero(tree, A):
    for x in range(0, len(A)):
        tree.insert(A[x])


def tempoinsert(tree, A):
    start = timer()
    crea_albero(tree, A)
    end = timer()
    return end - start


def tempofind(tree, n):
    k = int(np.random.rand() * n)
    start = timer()
    tree.find(k)
    end = timer()
    return end - start


def main():
    # tempiRinsertABR = []
    # tempiRinsertARN = []
    # tempiOinsertABR = []
    # tempiOinsertARN = []
    # temporicABRR = []
    # temporicARNR = []
    # temporicABRO = []
    # temporicARNO = []
    # e = open('randomInsert.txt', 'w')
    # e.write('Inserimentorandom\n')
    # e.write('Dimensione  ')
    # e.write(' ABR ')
    # e.write('  ARN\n')
    # f = open('RicercaRandom.txt', 'w')
    # f.write('RicercaRandom\n')
    # f.write('Dimensione  ')
    # f.write(' ABR ')
    # f.write('  ARN\n')
    # g = open('InsertOrdinato.txt', 'w')
    # g.write('inserimentoOrdinato\n')
    # g.write('Dimensione  ')
    # g.write(' ABR ')
    # g.write(' ARN\n')
    # h = open('RicercaOrdinata.txt', 'w')
    # h.write('Ordinato\n')
    # h.write('Dimensione  ')
    # h.write(' ABR ')
    # h.write(' ARN\n')
    # for j in range(10, 2000, 100):
    #     timeABRinsertR = 0
    #     timeARNinsertR = 0
    #     timeABRinsertO = 0
    #     timeARNinsertO = 0
    #     timeABRR = 0
    #     timeARNR = 0
    #     timeABRO = 0
    #     timeARNO = 0
    #     for i in range(1, 100):
    #         tree1 = ABR.ABR()
    #         tree2 = ARN.ARN()
    #         A = array(j)
    #         B = A[:]
    #         timeABRinsertR += tempoinsert(tree1, A)
    #         timeARNinsertR += tempoinsert(tree2, B)
    #         timeABRR += tempofind(tree1, j)
    #         timeARNR += tempofind(tree2, j)
    #         A.clear()
    #         B.clear()
    #
    #         tree1 = ABR.ABR()
    #         tree2 = ARN.ARN()
    #         A = array_ordinato(j)
    #         B = A[:]
    #         timeABRinsertO += tempoinsert(tree1, A)
    #         timeARNinsertO += tempoinsert(tree2, B)
    #         timeABRO += tempofind(tree1, j)
    #         timeARNO += tempofind(tree2, j)
    #         A.clear()
    #         B.clear()
    #
    #     tempiRinsertABR.insert(j, timeABRinsertR / i)
    #     tempiRinsertARN.insert(j, timeARNinsertR / i)
    #     e.write(str(j))
    #     e.write('  & ')
    #     e.write(str(round(timeABRinsertR / i, 4)))
    #     e.write('  & ')
    #     e.write(str(round(timeARNinsertR / i, 4)))
    #     e.write('\ \ \hline\n')
    #     temporicABRR.insert(j, timeABRR / i)
    #     temporicARNR.insert(j, timeARNR / i)
    #     f.write(str(j))
    #     f.write('  & ')
    #     f.write(str(round(timeABRR / i, 7)))
    #     f.write('  & ')
    #     f.write(str(round(timeARNR / i, 7)))
    #     f.write('\ \ \hline\n')
    #     tempiOinsertABR.insert(j, timeABRinsertO / i)
    #     tempiOinsertARN.insert(j, timeARNinsertO / i)
    #     g.write(str(j))
    #     g.write(' &  ')
    #     g.write(str(round(timeABRinsertO / i, 4)))
    #     g.write(' &  ')
    #     g.write(str(round(timeARNinsertO / i, 4)))
    #     g.write('\ \ \hline\n')
    #     temporicABRO.insert(j, timeABRO / i)
    #     temporicARNO.insert(j, timeARNO / i)
    #     h.write(str(j))
    #     h.write(' &  ')
    #     h.write(str(round(timeABRO / i, 4)))
    #     h.write(' &  ')
    #     h.write(str(round(timeARNO / i, 4)))
    #     h.write('\ \ \hline\n')
    #
    # x = np.arange(10, 2000, 100)
    # plt.plot(x, tempiRinsertABR, label="ABR")
    # plt.plot(x, tempiRinsertARN, label="ARN")
    # plt.legend()
    # plt.savefig('ABRrandom.png', bbox_inches='tight')
    # plt.close()
    # plt.plot(x, temporicABRR, label="ABR")
    # plt.plot(x, temporicARNR, label="ARN")
    # plt.legend()
    # plt.savefig('ABRricR.png', bbox_inches='tight')
    # plt.close()
    # plt.plot(x, tempiOinsertABR, label="ABR")
    # plt.plot(x, tempiOinsertARN, label="ARN")
    # plt.legend()
    # plt.savefig('ABRordinati.png', bbox_inches='tight')
    # plt.close()
    # plt.plot(x, temporicABRO, label="ABR")
    # plt.plot(x, temporicARNO, label="ARN")
    # plt.legend()
    # plt.savefig('ABRricO.png', bbox_inches='tight')
    # plt.close()
    # e.close()
    # f.close()
    # g.close()
    # h.close()

    tempiRinsertABR = []
    tempiRinsertARN = []
    tempiOinsertABR = []
    tempiOinsertARN = []
    temporicABRR = []
    temporicARNR = []
    temporicABRO = []
    temporicARNO = []
    e = open('randomInsert.txt', 'w')
    e.write('Inserimentorandom\n')
    e.write('Dimensione  ')
    e.write(' ABR ')
    e.write('  ARN\n')
    f = open('RicercaRandom.txt', 'w')
    f.write('RicercaRandom\n')
    f.write('Dimensione  ')
    f.write(' ABR ')
    f.write('  ARN\n')
    g = open('InsertOrdinato.txt', 'w')
    g.write('inserimentoOrdinato\n')
    g.write('Dimensione  ')
    g.write(' ABR ')
    g.write(' ARN\n')
    h = open('RicercaOrdinata.txt', 'w')
    h.write('Ordinato\n')
    h.write('Dimensione  ')
    h.write(' ABR ')
    h.write(' ARN\n')
    timeABRinsertR = np.zeros((21, 1))
    timeARNinsertR = np.zeros((21, 1))
    timeABRinsertO = np.zeros((21, 1))
    timeARNinsertO = np.zeros((21, 1))
    timeABRR = np.zeros((21, 1))
    timeARNR = np.zeros((21, 1))
    timeABRO = np.zeros((21, 1))
    timeARNO = np.zeros((21, 1))
    for i in range(1, 500):
        x = 0
        for j in range(10, 2000, 100):
            x += 1
            tree1 = ABR.ABR()
            tree2 = ARN.ARN()
            A = array(j)
            B = A[:]
            timeABRinsertR[x] += tempoinsert(tree1, A)
            timeARNinsertR[x] += tempoinsert(tree2, B)
            timeABRR[x] += tempofind(tree1, j)
            timeARNR[x] += tempofind(tree2, j)
            A.clear()
            B.clear()

            tree1 = ABR.ABR()
            tree2 = ARN.ARN()
            A = array_ordinato(j)
            B = A[:]
            timeABRinsertO[x] += tempoinsert(tree1, A)
            timeARNinsertO[x] += tempoinsert(tree2, B)
            timeABRO[x] += tempofind(tree1, j)
            timeARNO[x] += tempofind(tree2, j)
            A.clear()
            B.clear()
    x = 0
    for j in range(10, 2000, 100):
        x += 1
        tempiRinsertABR.insert(x, timeABRinsertR[x] / i)
        tempiRinsertARN.insert(x, timeARNinsertR[x] / i)
        if x % 4:
            e.write(str(j))
            e.write('  & ')
            e.write(str(timeABRinsertR[x] / i))
            e.write('  & ')
            e.write(str(timeARNinsertR[x] / i))
            e.write('\ \ \hline\n')
        temporicABRR.insert(x, timeABRR[x] / i)
        temporicARNR.insert(x, timeARNR[x] / i)
        if x % 4:
            f.write(str(j))
            f.write('  & ')
            f.write(str(timeABRR[x] / i))
            f.write('  & ')
            f.write(str(timeARNR[x] / i))
            f.write('\ \ \hline\n')
        tempiOinsertABR.insert(x, timeABRinsertO[x] / i)
        tempiOinsertARN.insert(x, timeARNinsertO[x] / i)
        if x % 4:
            g.write(str(j))
            g.write(' &  ')
            g.write(str(timeABRinsertO[x] / i))
            g.write(' &  ')
            g.write(str(timeARNinsertO[x] / i))
            g.write('\ \ \hline\n')
        temporicABRO.insert(x, timeABRO[x] / i)
        temporicARNO.insert(x, timeARNO[x] / i)
        if x % 4:
            h.write(str(j))
            h.write(' &  ')
            h.write(str(timeABRO[x] / i))
            h.write(' &  ')
            h.write(str(timeARNO[x] / i))
            h.write('\ \ \hline\n')

    x = np.arange(10, 2000, 100)
    plt.plot(x, tempiRinsertABR, label="ABR")
    plt.plot(x, tempiRinsertARN, label="ARN")
    plt.legend()
    plt.savefig('ABRrandom.png', bbox_inches='tight')
    plt.close()
    plt.plot(x, temporicABRR, label="ABR")
    plt.plot(x, temporicARNR, label="ARN")
    plt.legend()
    plt.savefig('ABRricR.png', bbox_inches='tight')
    plt.close()
    plt.plot(x, tempiOinsertABR, label="ABR")
    plt.plot(x, tempiOinsertARN, label="ARN")
    plt.legend()
    plt.savefig('ABRordinati.png', bbox_inches='tight')
    plt.close()
    plt.plot(x, temporicABRO, label="ABR")
    plt.plot(x, temporicARNO, label="ARN")
    plt.legend()
    plt.savefig('ABRricO.png', bbox_inches='tight')
    plt.close()
    e.close()
    f.close()
    g.close()
    h.close()


if __name__ == '__main__':
    main()
