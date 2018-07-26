from objectClients import *
class ArvoreCartoes():
    def __init__(self):
        self.none = Clients(0)
        self.none.setPai(self.none)
        self.none.setEsquerda(self.none)
        self.none.setDireita(self.none)
        self.none.setCor("Preto")
        self.raiz = self.none
    def inserir(self, nodoZ):
        nodoY = self.none
        nodoX = self.raiz
        while nodoX != self.none:
            nodoY = nodoX
            if nodoZ.getChave() < nodoX.getChave():
                nodoX = nodoX.getEsquerda()
            else:
                nodoX = nodoX.getDireita()
        nodoZ.setPai(nodoY)
        if nodoY == self.none:
            self.raiz = nodoZ
        elif nodoZ.getChave() < nodoX.getChave():
            nodoY.setEsquerda(nodoZ)
        else:
            nodoY.setDireita(nodoZ)
        nodoZ.setEsquerda(self.none)
        nodoZ.setDireita(self.none)
        nodoZ.setCor("Vermelho")

        self.consertaInserir(nodoZ)
    def consertaInserir(self, nodoZ):
        while nodoZ.getPai().cor is "Vermelho":
            if nodoZ.getPai() is nodoZ.getPai().getPai().getEsquerda():
                nodoY = nodoZ.getPai().getPai().getDireita()
                if nodoY.getCor() is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getDireita():
                        nodoZ = nodoZ.getPai()
                        rotacaoEsquerda(self,nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelha")
                    self.rotacaoDireita(nodoZ.getPai().getPai())
            else:
                nodoY = nodoZ.getPai().getPai().getEsquerda()
                if nodoY.getCor() is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getEsquerda():
                        nodoZ = nodoZ.getPai()
                        rotacaoDireita(self,nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    self.rotacaoEsquerda(nodoZ.getPai().getPai())
        self.raiz.setCor("Preto")
    def rotacaoEsquerda(self,nodoX):
        nodoY = nodoX.getDireita() #define y
        if nodoY is not self.none:
            nodoX.setDireita(nodoY.getEsquerda()) #Tranforna o filho esquerdo de y no filho direito de x
            if nodoY.getEsquerda() is not self.none:
                nodoY.getEsquerda().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is not self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getEsquerda():
                nodoX.getPai().setEsquerda(nodoY)
            else:
                nodoX.getPai().setDireita(nodoY)
            nodoY.setEsquerda(nodoX)
            nodoX.setPai(nodoY)
    def rotacaoDireita(self,nodoX):
        nodoY = nodoX.getEsquerda() #define y
        if nodoY is not self.none:
            nodoX.setEsquerda(nodoY.getDireita()) #Tranforna o filho direito de y no filho esquerdo de x
            if nodoY.getDireita() is not self.none:
                nodoY.getDireita().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is not self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getDireita():
                nodoX.getPai().setDireita(nodoY)
            else:
                nodoX.getPai().setEsquerda(nodoY)
            nodoY.setDireita(nodoX)
            nodoX.setPai(nodoY)
    def maximo(self, nodo):
        if nodo != None:
            while nodo.getDireita() != None:
                nodo = nodo.getDireita()
            return nodo
    def minimo(self, nodo):
        if nodo != self.none:
            while nodo.getEsquerda() != None:
                nodo = nodo.getEsquerda()
            return nodo
    def sucessor(self, nodo):
        if nodo.getDireita() != None:
            return self.minimo(nodo.getDireita())
        y = nodo.getPai()
        while y != None and nodo == y.getDireita():
            nodo = y
            y = y.getPai()
        if y is not None:
            return y.retornaValor()
    def transplante(self, a, b):
        pai_a = a.getPai()
        if pai_a == None:
            self.raiz = b
        elif a == pai_a.getEsquerda():
           pai_a.setEsquerda(b)
        else:
            pai_a.setDireita(b)
        b.setDireita(pai_a)
    def imprimeEmOrdem(self, nodo):
            if nodo is not self.none:
                self.imprimeEmOrdem(nodo.getEsquerda())
                print(str(nodo.getChave()), end=" ")
                self.imprimeEmOrdem(nodo.getDireita())
    def imprimePreOrdem(self, nodo):
        if nodo is not self.none:
            print(str(nodo.getChave()), end=" ")
            self.imprimePreOrdem(nodo.getEsquerda())
            self.imprimePreOrdem(nodo.getDireita())
    def imprimePosOrdem(self, nodo):
        if nodo is not self.none:
            self.imprimePosOrdem(nodo.getEsquerda())
            self.imprimePosOrdem(nodo.getDireita())
            print(str(nodo.getChave()), end=" ")
    def buscar(self,cartao,chave):
        if cartao is self.none or cartao.getDado() is chave:
            return cartao
        elif cahve < cartao.getDado():
            return self.buscar(cartao.getEsquerda(), chave)
        else:
            return self.buscar(cartao.getDireita(), chave)


class ArvoreEstabelecimentos():
    def __init__(self):
        self.none = Establishments(0)
        self.none.setPai(self.none)
        self.none.setEsquerda(self.none)
        self.none.setDireita(self.none)
        self.none.setCor("Preto")
        self.raiz = self.none
    def inserir(self, nodoZ):
        nodoY = self.none
        nodoX = self.raiz
        while nodoX != self.none:
            nodoY = nodoX
            if nodoZ.getChave() < nodoX.getChave():
                nodoX = nodoX.getEsquerda()
            else:
                nodoX = nodoX.getDireita()
        nodoZ.setPai(nodoY)
        if nodoY == self.none:
            self.raiz = nodoZ
        elif nodoZ.getChave() < nodoX.getChave():
            nodoY.setEsquerda(nodoZ)
        else:
            nodoY.setDireita(nodoZ)
        nodoZ.setEsquerda(self.none)
        nodoZ.setDireita(self.none)
        nodoZ.setCor("Vermelho")

        self.consertaInserir(nodoZ)
    def consertaInserir(self, nodoZ):
        while nodoZ.getPai().cor is "Vermelho":
            if nodoZ.getPai() is nodoZ.getPai().getPai().getEsquerda():
                nodoY = nodoZ.getPai().getPai().getDireita()
                if nodoY.getCor() is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getDireita():
                        nodoZ = nodoZ.getPai()
                        rotacaoEsquerda(self,nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelha")
                    self.rotacaoDireita(nodoZ.getPai().getPai())
            else:
                nodoY = nodoZ.getPai().getPai().getEsquerda()
                if nodoY.getCor() is "Vermelho":
                    nodoZ.getPai().setCor("Preto")
                    nodoY.setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    nodoZ = nodoZ.getPai().getPai()
                else:
                    if nodoZ is nodoZ.getPai().getEsquerda():
                        nodoZ = nodoZ.getPai()
                        rotacaoDireita(self,nodoZ)
                    nodoZ.getPai().setCor("Preto")
                    nodoZ.getPai().getPai().setCor("Vermelho")
                    self.rotacaoEsquerda(nodoZ.getPai().getPai())
        self.raiz.setCor("Preto")
    def rotacaoEsquerda(self,nodoX):
        nodoY = nodoX.getDireita() #define y
        if nodoY is not self.none:
            nodoX.setDireita(nodoY.getEsquerda()) #Tranforna o filho esquerdo de y no filho direito de x
            if nodoY.getEsquerda() is not self.none:
                nodoY.getEsquerda().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is not self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getEsquerda():
                nodoX.getPai().setEsquerda(nodoY)
            else:
                nodoX.getPai().setDireita(nodoY)
            nodoY.setEsquerda(nodoX)
            nodoX.setPai(nodoY)
    def rotacaoDireita(self,nodoX):
        nodoY = nodoX.getEsquerda() #define y
        if nodoY is not self.none:
            nodoX.setEsquerda(nodoY.getDireita()) #Tranforna o filho direito de y no filho esquerdo de x
            if nodoY.getDireita() is not self.none:
                nodoY.getDireita().setPai(nodoX) #Muda a progenitor de fato
            nodoY.setPai(nodoX.getPai())
            if nodoX.getPai() is not self.none:
                self.raiz = nodoY
            elif nodoX == nodoX.getPai().getDireita():
                nodoX.getPai().setDireita(nodoY)
            else:
                nodoX.getPai().setEsquerda(nodoY)
            nodoY.setDireita(nodoX)
            nodoX.setPai(nodoY)
    def maximo(self, nodo):
        if nodo != None:
            while nodo.getDireita() != None:
                nodo = nodo.getDireita()
            return nodo
    def minimo(self, nodo):
        if nodo != self.none:
            while nodo.getEsquerda() != None:
                nodo = nodo.getEsquerda()
            return nodo
    def sucessor(self, nodo):
        if nodo.getDireita() != None:
            return self.minimo(nodo.getDireita())
        y = nodo.getPai()
        while y != None and nodo == y.getDireita():
            nodo = y
            y = y.getPai()
        if y is not None:
            return y.retornaValor()
    def transplante(self, a, b):
        pai_a = a.getPai()
        if pai_a == None:
            self.raiz = b
        elif a == pai_a.getEsquerda():
           pai_a.setEsquerda(b)
        else:
            pai_a.setDireita(b)
        b.setDireita(pai_a)
    def imprimeEmOrdem(self, nodo):
            if nodo is not self.none:
                self.imprimeEmOrdem(nodo.getEsquerda())
                print(str(nodo.getChave()), end=" ")
                self.imprimeEmOrdem(nodo.getDireita())
    def imprimePreOrdem(self, nodo):
        if nodo is not self.none:
            print(str(nodo.getChave()), end=" ")
            self.imprimePreOrdem(nodo.getEsquerda())
            self.imprimePreOrdem(nodo.getDireita())
    def imprimePosOrdem(self, nodo):
        if nodo is not self.none:
            self.imprimePosOrdem(nodo.getEsquerda())
            self.imprimePosOrdem(nodo.getDireita())
            print(str(nodo.getChave()), end=" ")

    def buscar(self,estabelecimento,chave):
        if estabelecimento is self.none or estabelecimento.getDado() is chave:
            return estabelecimento
        elif cahve < estabelecimento.getDado():
            return self.buscar(estabelecimento.getEsquerda(), chave)
        else:
            return self.buscar(estabelecimento.getDireita(), chave)
