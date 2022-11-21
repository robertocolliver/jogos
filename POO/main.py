from player import *
from karos import *

def selecionar_personagem(eu):
    print(f'{eu} Selecione um personagem')
    
    paladina = Paladina(espada=True, escudo=True, level='1', nome ='paladina', classe='paladina')
    assassino = Vampiro(adaga=True, level='1', nome='assassino', classe='assassino')
    
    print('1', paladina) 
    print('2', assassino)   


    while True: 
        
        escolha = input('Escolha um personagem: ')
    
        if escolha == '1':
            eu.escolher_personagem(paladina)
            break
        elif escolha == '2':
            eu.escolher_personagem(assassino)
            break
        else:
            print('inválido!')

eu = Jogadores(nome='EU')
print(eu)
