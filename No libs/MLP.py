from Camadas import Camada
class MLP():
    def __init__(self,entradas,neuronios_em_camadas):
        self.camadas=[]
        self.camadas.append(Camada(entradas,neuronios_em_camadas[0]))
        for i,n in enumerate(neuronios_em_camadas[1:]):
            self.camadas.append(Camada(neuronios_em_camadas[i],n))

    def __call__(self,entradas):
        saida = entradas
        for c in self.camadas:
            saida=c(saida)
        return saida
    def params(self):
        parametros=[]
        for c in self.camadas:
            parametros+=c.params()
        return parametros