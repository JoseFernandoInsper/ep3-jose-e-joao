
import tkinter as tk
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
    
matriz_jogo = zeros([3,3])

class InterfaceJogo:
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.geometry("300x320+540+200")
        self.tabuleiro.title("Jogo da Velha")
        self.tabuleiro.rowconfigure(0, minsize=100)
        self.tabuleiro.rowconfigure(1, minsize=100)
        self.tabuleiro.rowconfigure(2, minsize=100)
        self.tabuleiro.columnconfigure(0, minsize=100)
        self.tabuleiro.columnconfigure(1, minsize=100)
        self.tabuleiro.columnconfigure(2, minsize=100)
        
        
        self.botao_1 = tk.Button(self.tabuleiro)
        self.botao_1.configure(bg="yellow", command=self.botao_1_clicado)
        self.botao_1.grid(row= 0, column= 0, sticky= "nwse")
        
        self.botao_2 = tk.Button(self.tabuleiro)
        self.botao_2.configure(bg="yellow", command=self.botao_2_clicado)
        self.botao_2.grid(row= 0, column= 1, sticky= "nwse")
        
        self.botao_3 = tk.Button(self.tabuleiro)
        self.botao_3.configure(bg="yellow", command=self.botao_3_clicado)        
        self.botao_3.grid(row= 0, column= 2, sticky= "nwse")
        
        self.botao_4 = tk.Button(self.tabuleiro)
        self.botao_4.configure(bg="yellow", command=self.botao_4_clicado)
        self.botao_4.grid(row= 1, column= 0, sticky= "nwse")
        
        self.botao_5 = tk.Button(self.tabuleiro)
        self.botao_5.configure(bg="yellow", command=self.botao_5_clicado)
        self.botao_5.grid(row= 1, column= 1, sticky= "nwse")
        
        self.botao_6 = tk.Button(self.tabuleiro)
        self.botao_6.configure(bg="yellow", command=self.botao_6_clicado)
        self.botao_6.grid(row= 1, column= 2, sticky= "nwse")
        
        self.botao_7 = tk.Button(self.tabuleiro)
        self.botao_7.configure(bg="yellow", command=self.botao_7_clicado)
        self.botao_7.grid(row= 2, column= 0, sticky= "nwse")

        self.botao_8 = tk.Button(self.tabuleiro)
        self.botao_8.configure(bg="yellow", command=self.botao_8_clicado)
        self.botao_8.grid(row= 2, column= 1, sticky= "nwse")
        
        self.botao_9 = tk.Button(self.tabuleiro)
        self.botao_9.configure(bg="yellow", command=self.botao_9_clicado)
        self.botao_9.grid(row= 2, column= 2, sticky= "nwse")
        
        self.visor = tk.Label(self.tabuleiro)
        self.visor.grid(row= 3, column= 0, columnspan=3, sticky="nwse")
        self.visor.configure(bg= "blue", text="jogador: "  ) 
        
    
    def botao_1_clicado(self):
        
        self.botao_1.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[0,0] = 1
    
    def botao_2_clicado(self):
        self.adicionar_jogada(2)
        self.botao_2.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[0,1] = 1
        
    def botao_3_clicado(self):
        self.adicionar_jogada(3)
        self.botao_3.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[0,2] = 1
 
    def botao_4_clicado(self):
        self.adicionar_jogada(4)
        self.botao_4.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[1,0] = 1
    
    def botao_5_clicado(self):
        self.adicionar_jogada(5)
        self.botao_5.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[1,1] = 1
        
    def botao_6_clicado(self):
        self.adicionar_jogada(6)
        self.botao_6.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[1,2] = 1
        
    def botao_7_clicado(self):
        self.adicionar_jogada(7)
        self.botao_7.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[2,0] = 1
        
    def botao_8_clicado(self):
        self.adicionar_jogada(8)
        self.botao_8.configure(text="x", font= "Arial 35 bold", state="disabled")
        matriz_jogo[2,1] = 1
        
    def botao_9_clicado(self):
        self.adicionar_jogada(9)
        self.botao_9.configure(text="x", font= "Arial 35 bold", state="disabled")        
        matriz_jogo[2,2] = 1
        
    def iniciar(self):
        self.tabuleiro.mainloop()
        
    def adicionar_jogada(self, b):
        print("botao_{0}_clicado".format(b))
        
        


objjogo = jogo()
play = InterfaceJogo()
play.iniciar()
print(matriz_jogo)