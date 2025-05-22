from sklearn.linear_model import LinearRegression
import numpy as np
x = [5, 10, 15, 20, 25, 35]
y = [14, 28, 30, 38, 44, 50]

X = np.array(x).reshape(-1,1)
Y = np.array(y).reshape(-1,1)

modelo = LinearRegression()
modelo.fit(X, Y)


entrada = float(input('x: '))  
H = np.array([[entrada]])      

# Previsão
previsao = modelo.predict(H)
print(f'Previsão para x={entrada}: {previsao[0][0]:.2f}')