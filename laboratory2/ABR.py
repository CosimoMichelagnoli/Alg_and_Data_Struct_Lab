import sys
import random
import numpy as np
from timeit import default_timer as timer

sys.setrecursionlimit(15000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.dad = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def getFather(self):
        return self.dad


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, current_node, key):
        if key <= current_node.key:
            if current_node.left:
                self.insertNode(current_node.left, key)
            else:
                current_node.left = Node(key)
                current_node.left.dad = current_node
        elif key > current_node.key:
            if current_node.right:
                self.insertNode(current_node.right, key)
            else:
                current_node.right = Node(key)
                current_node.right.dad = current_node

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, current_node, key):
        if current_node is None:
            return False
        elif key == current_node.key:
            return True
        elif key < current_node.key:
            return self.findNode(current_node.left, key)
        else:
            return self.findNode(current_node.right, key)

    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            # print(v.key)
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)


def crea_casualmente(abr, n):
    for x in range(0, n):
        abr.insert(np.random.randint(1, 100))


def crea_ordinati(abr, n):
    for x in range(0, n):
        abr.insert(x)


def main():
    n = 100
    tree = ABR()
    print("Analisi su ABR di ", n, " elementi{")
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento con ordine casuale è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a=tree.find(random.randrange(1,100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=",a," è: ", end - start)
    print("\n")
    tree = ABR()
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento in ordine è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("}\n")
    print("\n")

    n = 1000
    tree = ABR()
    print("Analisi su ABR di ", n, " elementi{")
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento con ordine casuale è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("\n")

    tree = ABR()
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento in ordine è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("}\n")
    print("\n")

    n = 10000
    tree = ABR()
    print("Analisi su ABR di ", n, " elementi{")
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento con ordine casuale è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("\n")

    tree = ABR()
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento in ordine è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    print("}\n")
    print("\n")

    n = 100000
    tree = ABR()
    print("Analisi su ABR di ", n, " elementi{")
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento con ordine casuale è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("\n")


    tree = ABR()
    start = timer()
    crea_casualmente(tree, n)
    end = timer()
    print("Il tempo impiegato per l' inserimento in ordine è: ", end - start)
    start = timer()
    tree.inorder()
    end = timer()
    print("Il tempo impiegato per la visita è: ", end - start)
    start = timer()
    a = tree.find(random.randrange(1, 100))
    end = timer()
    print("Il tempo impiegato per ricerca con successo=", a, " è: ", end - start)
    print("}\n")
    print("\n")


if __name__ == "__main__":
    main()
