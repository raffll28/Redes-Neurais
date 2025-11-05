from Derivada import Derivada
import random
class No():
    def __init__(self, qtd_en):
        self.pesos =  [Derivada(random.randrange(-100,100)/100) for _ in range(qtd_en)]
        self.vies = Derivada(random.randrange(-100,100)/100)
    def __call__(self,entradas):
        saida= Derivada(0)
        saida= self.vies+saida
        for i,p in enumerate(self.pesos):
            saida+= p*entradas[i]
        return saida.sig()
    
    def params(self):
        return self.pesos+[self.vies]

