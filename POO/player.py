from karos import Paladina, Vampiro
import random 

npcs = ['Rodrigo', 'Camilla', 'Renata', 'Fernanda', 'Beatriz', 'Maria']
personagem_npcs = ['atirador', 'paladina', 'maga', 'feitiçeira', 'guerreiro', 'assassino']

class Pessoas:
    
    def __init__(self, nome=None, personagens=[]):
        self.nome = random.choice(npcs)
        self.personagens = personagens

    
    def __str__(self):
        return self.nome


    def mostrar_personagens(self):
        if personagens:
            for c in self.personagens:
                print(c, end='  ')
        else:
            print('Não tem personagens')

class jogadores(Pessoas): 
    tipo = 'jogador'
   
    lista_jogador = []
    def escolher_personagem(self, personagem):
        self.lista_jogador.append(personagem)
        print(personagem)

class Inimigos(Pessoas):
    tipo = 'inimigo'
    
    def __init__(self, nome=None, personagens=[]):
        super().__init__(nome=nome, personagens=personagens)
        
        if not personagens:
            for c in range(1, 5):
                personagens.append(random.choice(personagem_npcs))



assassino = Vampiro(adaga=True, nome='Renato', level='1')
paladina = Paladina(espada=True, escudo=True, nome='Carolis', level=1, classe='Templaria')
eu = jogadores(nome='Roberto', personagens=[assassino, paladina])
eu.mostrar_personagens()
