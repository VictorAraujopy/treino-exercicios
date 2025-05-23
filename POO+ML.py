#Exercício POO júnior: Classe Carro
from sklearn.linear_model import LogisticRegression
import numpy as np



class Carro_bom_ruim():
    def __init__(self):
        x = [2008, 2020, 2001, 1999]
        y = [1, 1, 0, 0]

        X = np.array(x).reshape(-1,1)
     
        self.modelo = LogisticRegression()

        self.modelo.fit(X,y)

    def prever_bom_ruim(self):

        self.ano = int(input('ano'))
        self.reform = np.array([[self.ano]])
        self.previsao = self.modelo.predict(self.reform)[0]

    def mostrar(self):
        if self.previsao > 0:
            print("seu carro é bom")

        else:
            print("carro ruim")


C = Carro_bom_ruim()
C.prever_bom_ruim()
C.mostrar()



