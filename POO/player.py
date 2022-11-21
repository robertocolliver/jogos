import random 
from karos import *


npcs = ['Rodrigo', 'Camilla', 'Renata', 'Fernanda', 'Beatriz', 'Maria']
personagem_npcs = ['atirador', 'paladina', 'maga', 'feitiçeira', 'guerreiro', 'assassino']

class Pessoas:
    
    def __init__(self, nome=None, personagens=[]):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(npcs)
        
        self.personagens = personagens
    
    def __str__(self):
        return self.nome


    def mostrar_personagens(self):
        if self.personagens:
            for c in self.personagens:
                print(c, end='  ')
        else:
            print('Não tem personagens')

class Jogadores(Pessoas): 
    tipo = 'jogador'
   
    lista_jogador = []
    def escolher_personagem(self, personagem):
        self.personagens_lista.append(personagem)
        print('{self} escolheu {personagem}')

class Inimigos(Pessoas):
    
    tipo = 'inimigo'

    def __init__(self, nome, personagens=[]):
        super().__init__(nome=nome, personagens=personagens)
        
        if not personagens:
            for c in range(1, 6):
                personagens.append(random.choice(personagem_npcs))


