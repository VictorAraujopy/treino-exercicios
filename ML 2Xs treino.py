from sklearn.linear_model import LogisticRegression
import numpy as np

#horas de estudo
x1 = [5, 1, 3, 0]
#nota
x2 = [10,4 , 8, 1]
#passou ou não
y = [1,0,1,0]

# deixa a matriz 2D
X = np.array([x1, x2]).T

Y = np.array(y)


#define o modelo
modelo = LogisticRegression()
#treina
modelo.fit(X,Y)

entrada = float(input('horas de estudo'))
Notas = float(input("qual foi sua nota"))
#reforma a entrada pro tipo certo de lista/matriz
reform = np.array([[entrada, Notas]])

previsao = modelo.predict(reform)

if previsao  > 0:
    print('vc passou')
else:
    print('não passou')