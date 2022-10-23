from random import randint


class Adversario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido
        self.doces = 0
        
        if self.apelido == "Rancoroso":
            self.rancoroso = True # ver isto depois na hora

    
    def jogada(self, jogada_do_ninja):
        doces_para_o_ninja = 0
        if jogada_do_ninja == "Doçura":
            x = 20
            # FALTA ISTO
            
        elif jogada_do_ninja == "Travessura":
            x = 10
            # FALTA ISTO

        return doces_para_o_ninja

'''
Descrição dos adversários:
Bruxa Bondosa - Joga sempre doçura
Esqueleto Egoísta - Joga sempre travessura
Palhaço Plagiário - Copia sempre a tua última jogada
Robot Rancoroso - Joga sempre doçura, até que jogues travessura. A partir daí joga sempre travessura.
'''
bruxa = Adversario(nome="Bruxa", apelido="Bondosa")
esqueleto = Adversario(nome="Esqueleto", apelido="Egoísta")
palhaco = Adversario(nome="Palhaço", apelido="Plagiário")
robot = Adversario(nome="Robô", apelido="Rancoroso")

adversarios = [bruxa, esqueleto, palhaco, robot]


rodada = 0
doces_ninja = 0
doces_adversario = 0

adversario = adversarios[randint(0,len(adversarios) -1)]
while rodada <= 10:
    decisaoNinja = input("Digite doçura ou travessura: ")
    
    jogada_do_adversario = adversario.jogada(jogada_do_ninja=decisaoNinja)

    doces_ninja += jogada_do_adversario

    rodada += 1