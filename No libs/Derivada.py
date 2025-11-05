import math

class Derivada:
    def __init__(self,num):
        self.num = num
        self.grad = 0
        self.anteriores = ()
        self.backward = lambda: None

    def __str__(self):
        return f"num: {self.num} grad: {self.grad} anteriores {[item.num for item in self.anteriores]}"
    
    def __add__(self, outraClasse):
        novaClasse =  Derivada(self.num + outraClasse.num)
        novaClasse.anteriores = (self, outraClasse)
        def drv_adição():
            self.grad += 1 * novaClasse.grad
            outraClasse.grad += 1 * novaClasse.grad
        novaClasse.backward = drv_adição
        return novaClasse

    def __mul__(self, outraClasse):
        novaClasse =  Derivada(self.num * outraClasse.num)
        novaClasse.anteriores = (self, outraClasse)
        def drv_multiplicação():
            self.grad += outraClasse.num * novaClasse.grad
            outraClasse.grad += self.num * novaClasse.grad
        novaClasse.backward = drv_multiplicação
        return novaClasse
    
    def sig(self):
        x = self.num

        if(x > 15):
            sigx = 0.99999
        elif(x < -15):
            sigx = 0.00001
        else:
            sigx = 1/(1+math.exp(-x))

        novo = Derivada(sigx)
        novo.anteriores = (self,)
        def drv_sig():
            self.grad += sigx*(1-sigx)*novo.grad
        novo.backward = drv_sig
        return novo
    
    def derivar_todos_anteriores(self):
        def ordem_contrutor(no:Derivada):
            if no not in visitados:
                visitados.add(no)
                for var in no.anteriores:
                    ordem_contrutor(var)
                ordem.append(no)
        
        ordem = []
        visitados = set()
        ordem_contrutor(self)

        self.grad = 1
        for dr in reversed(ordem):
            dr.backward()
    

