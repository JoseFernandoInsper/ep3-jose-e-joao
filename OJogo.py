from numpy import zeros
class jogo(object):  
    def __init__(self):
        self.jogador_atual = 1
            
    def recebe_jogada(self,linha,coluna):
# Caso o jogador tente alterar a jogada anterior       
       if (matriz_jogo[linha,coluna] != 0):
          print("Jogada Invalida")
          return 0
           
       else:    
           matriz_jogo[linha,coluna]=self.jogador_atual       
           if (self.jogador_atual == 1):
               self.jogador_atual =2
               print ("vez do x")
           else:
                self.jogador_atual = 1
                print("vez do O")            
    

    '''def verifica_gnhador():
        len matriz_jogo
    #verifica se há simbolos alinhados
        if #nenhum alinhado:
            return 0
        elif #X alinhado:
        return 1
    elif #O alinhado:
        return 2
        
        
    def limpa_jogada():
        if verifica_ganhador==True:
            #transforma a matriz em uma matriz de zeros'''
    

  
matriz_jogo = zeros([3,3])

objjogo = jogo()

objjogo.recebe_jogada(0,1)
print (matriz_jogo)

objjogo.recebe_jogada(0,0)
print(matriz_jogo)

objjogo.recebe_jogada(0,0)
print(matriz_jogo)

objjogo.recebe_jogada(1,0)
print(matriz_jogo)

objjogo.recebe_jogada(2,2)
print(matriz_jogo)