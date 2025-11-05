from Derivada import Derivada
from No import No
from Camadas import Camada
from MLP import MLP

x = [
    [Derivada(-1)],
    [Derivada(0)],
    [Derivada(1.0)]
]
y = [Derivada(2), Derivada(1), Derivada(2.0)]

rede = MLP(1,[50,30,1])

tx_ap = 0.1
for i in range(500):
    erro_acumulado =Derivada(0)
    for e,s in zip(x,y):
        y_f = rede(e)[0]
        menos_y=Derivada(-1)*s
        erro = (y_f+menos_y)
        erro_quadrado=erro*erro
        erro_acumulado+=erro_quadrado
    print(f"erro_acumulado {erro_acumulado}")
    erro_acumulado.derivar_todos_anteriores()
    for p in rede.params():
        p.num += -p.grad * tx_ap #Adam()
        p.grad=0