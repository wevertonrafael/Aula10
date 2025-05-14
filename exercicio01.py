class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

        def comer(self):
            print(f"O seu {self.nome} foi comer...")

class Gato(Animal):
            def __init__(self,nome,cor):
                super().__init__(nome,cor)

            def miar(self):
                print(f"{self.nome} foi miando o tempo todo...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"{self.nome} o cachorro latiu muito...")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def moo(self):
        print(f"{self.nome} A minha vaca tá agitada")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def pula(self):
        print(f"O meu {self.nome} salta muito")

class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def imprimeValor(self):
        print(f"O preço do {self.valor} é ")

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor*1.5)

class Forma():
    def __init__(self):
        self.area=0
        self.perimentro=0

class Retangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura

    def calculaArea(self):
        self.area=self.base*self.altura
        print(self.area)

    def calculaPerimentro(self):
        self.perimentro=2*(self.base+self.altura)
        print(self.perimentro)

class Triangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area=3*self.base
        print(self.area)

    def calculaPerimentro(self):
        self.perimentro = (self.base*self.altura)/2
        print(self.perimentro)


