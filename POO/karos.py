class Personagem: 
  
  def __init__(self, tipo, raça, nome=None, level=1):
    self.tipo = tipo 
    self.raça = raça
    self.nome = nome 
    self.level = level 
  
  def __str__(self):
    return f'{self.nome}({self.level}) {self.raça} {self.tipo}'

  def atacar(self, personagem):
    print(f'{self} ataca {personagem}')

class Paladina(Personagem): 
  
  def __init__(self, espada, escudo, tipo, raça, nome):
    super().__init__(tipo,raça, nome)
    self.espada = espada 
    self.escudo = escudo
  
class Vampiro(Personagem):
  
  def __init__(self, adaga, tipo, raça, nome):
    super().__init__(tipo, raça, nome)
    self.adaga = adaga 


paladina = Paladina(True, True, 'suporte', 'humana', 'Carolina')
assassino = Vampiro(True, 'assassino', 'guerreiro', 'Robson')

paladina.atacar(assassino)