from OJogo import jogo
import tkinter as tk
import tkinter.messagebox as tkm

class InterfaceJogo:
    def __init__(self):
        self.objjogo = jogo()
        
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
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
    def botao_1_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_1.configure(text="X", font= "Arial 35 bold", state="disabled")
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        else:
            self.botao_1.configure(text="O", font= "Arial 35 bold", state="disabled")
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        self.objjogo.recebe_jogada(0,0)
        
        self.caixa_mensagem()
        
        
        
        
    def botao_2_clicado(self):
        if self.objjogo.jogador_atual== 1 :
            self.botao_2.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_2.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(0,1)
        
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
            
        self.caixa_mensagem()
       
    def botao_3_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_3.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_3.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(0,2)
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        
        else :
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()
        
                        
                
    def botao_4_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_4.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_4.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(1,0)
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
            
        self.caixa_mensagem()

    def botao_5_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_5.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_5.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(1,1)
        
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()

    def botao_6_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_6.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_6.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(1,2)
        
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()

    def botao_7_clicado(self):
        if self.objjogo.jogador_atual == 1:
            self.botao_7.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_7.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(2,0)
        
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()

    def botao_8_clicado(self):
        if self.objjogo.jogador_atual == 1:
            self.botao_8.configure(text="X", font= "Arial 35 bold", state="disabled")
        else:
            self.botao_8.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(2,1)
        
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()

    def botao_9_clicado(self):
        if self.objjogo.jogador_atual == 1 :
            self.botao_9.configure(text="X", font= "Arial 35 bold", state="disabled")
        else :
            self.botao_9.configure(text="O", font= "Arial 35 bold", state="disabled")
        self.objjogo.recebe_jogada(2,2)
        if self.objjogo.jogador_atual == 1 :
            self.visor.configure(bg= "blue", text="jogador: Vez do X")
        else:
            self.visor.configure(bg= "blue", text="jogador: Vez do O")
        
        self.caixa_mensagem()
            
    def caixa_mensagem(self):
        resultado = self.objjogo.verifica_ganhador()
        if resultado == 0:
            tkm.showinfo(title="Game Over", message = "Deu Velha")
        elif resultado == 1:
            #vitoria X
            pass
        elif resultado == 2:
            #vitoria O
            pass
        

    def iniciar(self):
        self.tabuleiro.mainloop()

play = InterfaceJogo()
play.iniciar()
