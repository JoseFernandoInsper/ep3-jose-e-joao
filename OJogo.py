from numpy import zeros

class jogo(object):  
    def __init__(self):
        self.jogador_atual = 1
            
    def recebe_jogada(self,linha,coluna):
          
           matriz_jogo[linha,coluna]=self.jogador_atual       
           if (self.jogador_atual == 1):
               self.jogador_atual =5
               print ("vez do x")
           else:
                self.jogador_atual = 1
                print("vez do O")            
    

    def verifica_ganhador():
        if sum(matriz_jogo.flat[:])==25:
            print("Deu Velha")            
        
        '''elif #X alinhado:
        return 1
    elif #O alinhado:
        return 2'''
        
        
    '''def limpa_jogada():
        if verifica_ganhador==True:
            #transforma a matriz em uma matriz de zeros'''
    
  
matriz_jogo = zeros([3,3])
print (matriz_jogo[2][2])
objjogo = jogo()

objjogo.recebe_jogada(0,0)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(0,1)
#objjogo.verifica_ganhador
print (matriz_jogo)


objjogo.recebe_jogada(0,2)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(1,0)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(1,1)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(1,2)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(2,0)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(2,1)
#objjogo.verifica_ganhador
print (matriz_jogo)

objjogo.recebe_jogada(2,2)
#objjogo.verifica_ganhador
print (matriz_jogo)

matriz_jogo
objjogo.verifica_ganhador
if sum(matriz_jogo.flat[:])==25:
            print("Deu Velha!!!")   