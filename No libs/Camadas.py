from No import No
class Camada():
    def __init__(self,qtd_entradas,qtd_nos):
        self.nos = [No(qtd_entradas) for _ in range(qtd_nos)]
    def __call__(self,entradas):
        return [no(entradas) for no in self.nos]
    def params(self):
        parametros = []
        for no in self.nos:
            parametros+=no.params()
        return parametros