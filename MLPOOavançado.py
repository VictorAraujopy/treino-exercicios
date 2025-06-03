from sklearn.linear_model import LogisticRegression
import numpy as np

class  Alunos():

 def __init__(Self):
  
  Self.alunos = ["rogerio", "claudio", "roberto", "lais","claudio"]
  Self.notas = [10, 7, 6, 4, 3]
  Self.passou =[1, 1, 0, 0, 0]
  
 

 def adicionar(Self):
    addnome = str(input("seu nome"))
    addnota = int(input('sua nota'))
    
    Self.alunos.append(addnome)
    Self.notas.append(addnota)

    

 def passou_y_n(Self):
    X = np.array(Self.notas[:-1]).reshape(-1, 1)
    Y= Self.passou
    
    
    
    Self.modelo = LogisticRegression()      
    Self.modelo.fit(X,Y)
    Self.todas_notas = np.array(Self.notas).reshape(-1, 1)
    Self.previsao = Self.modelo.predict(Self.todas_notas)

    print("Resultado dos alunos:")
    for nome, resultado in zip(Self.alunos, Self.previsao):
            if resultado == 1:
                status = "✅ Passou"
            else:
                status = "❌ Reprovou"
            print(f"{nome}: {status}")

al = Alunos()

al.adicionar()
al.passou_y_n()







    