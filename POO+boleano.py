



class biblioteca():
    def __init__(self):
        self.titulos = {"kick ass" : True,
                        
                        "sandman" : True,
                         "sherek": False}
      

    def desejo(self):
        opção = int(input("o que vc deseja? 1 para adicionar/devolver ou 2 para pedir"))
        if opção == 1:
            bibi.adicionar()
        if opção ==2:
            bibi.pedir()
        

    def pedir(self):
        
        self.pedido = str(input("peça seu livro"))
        if self.pedido in self.titulos:
            bibi.disponivel()
        else:
            print("livro não existe")

    def disponivel(self):
        
        if self.titulos[self.pedido] == True:
            print ("livro emprestado")
            self.titulos[self.pedido] = False

        else:
            print("livro não diponivel")

    def adicionar(self):
        
        add = str(input("digite o livro que deseja adicionar:"))
        if add not in self.titulos:
            self.titulos[add] = True
            print(f"livro: {add}, devolvido")
        else:
            print("livro adicionado")
       




bibi = biblioteca()
bibi.desejo()