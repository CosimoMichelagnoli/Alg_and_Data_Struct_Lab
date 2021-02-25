import Insertion_sort
import Quick_sort
import numpy as np
from timeit import default_timer as timer
import matplotlib
import matplotlib.pyplot as plt


def array(A, n):
    for i in range(0, n):
        A.insert(i, int(np.random.rand() * 100))


def array_ordinato_al_contrario(A, n, k):
    k = k * k
    array_ordinato(A, n, k)
    A.reverse()


def array_ordinato(A, n, k):
    for i in range(0, n):
        A.insert(i, i * k)


def timeinsertion_sort(A):
    start = timer()
    Insertion_sort.insertion_sort(A)
    end = timer()
    return end - start


def timequick_sort(B, p, r):
    start = timer()
    Quick_sort.quick_sort(B, p, r)
    end = timer()
    return end - start


def main():
    f = open('blun7random.txt', 'w')
    f.write('random\n')
    f.write('Dimensione  ')
    f.write(' insertion ')
    f.write('  quick\n')
    g = open('blun8ordinato.txt', 'w')
    g.write('ordinato\n')
    g.write('Dimensione  ')
    g.write(' insertion ')
    g.write(' quick\n')
    h = open('blun9reverse.txt', 'w')
    h.write('reverse\n')
    h.write('Dimensione  ')
    h.write(' insertion ')
    h.write(' quick\n')
    A = []
    tempoquickR = []
    tempoinsertionR = []
    tempoquickO = []
    tempoinsertionO = []
    tempoquickC = []
    tempoinsertionC = []
    for j in range(1, 4000, 100):
        timeINR = 0
        timeQUR = 0
        timeINC = 0
        timeQUC = 0
        timeINO = 0
        timeQUO = 0
        for i in range(1, 25):
            array(A, j)
            B = A[:]
            # print(A)
            timeINR += timeinsertion_sort(A)
            timeQUR += timequick_sort(B, 0, j - 1)
            A.clear()
            B.clear()

            array_ordinato(A, j, i)
            B = A[:]
            timeINO += timeinsertion_sort(A)
            timeQUO += timequick_sort(B, 0, j - 1)
            A.clear()
            B.clear()

            array_ordinato_al_contrario(A, j, i)
            B = A[:]
            timeINC += timeinsertion_sort(A)
            timeQUC += timequick_sort(B, 0, j - 1)
            A.clear()
            B.clear()

        tempoinsertionR.insert(j, timeINR / i)
        tempoquickR.insert(j, timeQUR / i)
        f.write(str(j))
        f.write('  & ')
        f.write(str(round(timeINR / i, 4)))
        f.write('  & ')
        f.write(str(round(timeQUR / i, 4)))
        f.write('\ \ \hline\n')
        tempoinsertionO.insert(j, timeINO / i)
        tempoquickO.insert(j, timeQUO / i)
        g.write(str(j))
        g.write(' &  ')
        g.write(str(round(timeINO / i, 4)))
        g.write(' &  ')
        g.write(str(round(timeQUO / i,4)))
        g.write('\ \ \hline\n')
        tempoinsertionC.insert(j, timeINC / i)
        tempoquickC.insert(j, timeQUC / i)
        h.write(str(j))
        h.write(' &  ')
        h.write(str(round(timeINC / i, 4)))
        h.write(' &  ')
        h.write(str(round(timeQUC / i, 4)))
        h.write('\ \ \hline\n')

    x = np.arange(1, 4000, 100)
    plt.plot(x, tempoinsertionR, label="Insertion-sort")
    plt.plot(x, tempoquickR, label="Quick-sort")
    plt.legend()
    plt.savefig('random.png', bbox_inches='tight')
    plt.close()
    plt.plot(x, tempoinsertionO, label="Insertion-sort")
    plt.plot(x, tempoquickO, label="Quick-sort")
    plt.legend()
    plt.savefig('ordinati.png', bbox_inches='tight')
    plt.close()
    plt.plot(x, tempoinsertionC, label="Insertion-sort")
    plt.plot(x, tempoquickC, label="Quick-sort")
    plt.legend()
    plt.savefig('ordine_inverso.png', bbox_inches='tight')
    f.close()
    g.close()
    h.close()


if __name__ == '__main__':
    main()
