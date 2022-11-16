from karos import Paladina, Vampiro

class Pessoas:
    
    def __init__(self, nome=None, personagens=[]):
        if nome:
            self.nome = nome
        else: 
            self.nome = 'NPC'
        
        self.personagens = personagens

    def __str__(self):
        return self.nome


    def mostrar_personagens(self):
        for c in self.personagens:
            print(c, end='  ')


class jogadores(Pessoas):
    tipo = 'jogador'
    


class vendedores(Pessoas):
    tipo = 'vendedores'


class inimigos(Pessoas):
    tipo = 'inimigo'


paladina = Paladina(True, True, 'Carolina', level=1)
assassino = Vampiro(True, 'Robson', level=1)



jogador = jogadores(nome='Roberto', personagens=[paladina, assassino])
print(jogador.nome)
jogador.mostrar_personagens()
