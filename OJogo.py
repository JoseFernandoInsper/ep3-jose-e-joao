from numpy import zeros

class jogo(object):  
    def __init__(self):
        self.matriz_jogo = zeros([3,3])
        self.jogador_atual = 1
            
    def recebe_jogada(self,linha,coluna):
          
           self.matriz_jogo[linha,coluna]=self.jogador_atual       
           if (self.jogador_atual == 1):
               self.jogador_atual =5
               print ("vez do x")
           else:
                self.jogador_atual = 1
                print("vez do O")            
    
    

    def verifica_ganhador(self):
#        if self.matriz_jogo[0][0] == self.matriz_jogo[0][1] == self.matriz_jogo[0][2] == 1 or \
#           self.matriz_jogo[1][0] == self.matriz_jogo[1][1] == self.matriz_jogo[1][2] == 1 or \
#           self.matriz_jogo[2][0] == self.matriz_jogo[2][1] == self.matriz_jogo[2][2] == 1 or \
#           self.matriz_jogo[0][0] == self.matriz_jogo[1][0] == self.matriz_jogo[2][0] == 1 or \
#           return 1
        pass

        
        '''elif #X alinhado:
        return 1
    elif #O alinhado:
        return 2'''
        
        
    '''def limpa_jogada():
        if verifica_ganhador==True:
            #transforma a matriz em uma matriz de zeros'''
