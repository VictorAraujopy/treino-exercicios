###Exercício 1 — Classe Pessoa Crie uma classe chamada Pessoa que tenha os atributos: nome (string) idade (inteiro)
### E um método chamado fazer_aniversario() que aumenta a idade da pessoa em 1. Crie um método que imprima uma frase com o nome e a idade da pessoa.






class Pessoa():
    def __init__ (self):

        nome = str(input("me diga seu nome"))
        idade = int(input("idade"))
        self.nome = nome
        self.idade = idade



    def fazer_aniversario(self):
        self.idade += 1

        print("pós aniversário")



    def mostrar_dados(self):

        print(f"{self.nome}, {self.idade}")

p = Pessoa()


p.mostrar_dados()
p.fazer_aniversario()
p.mostrar_dados()