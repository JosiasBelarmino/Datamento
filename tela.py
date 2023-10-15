from tkinter import *
root = Tk()

class application():
    def __init__ (self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()
    def tela(self):
        self.root.title("Datamento")
        self.root.configure(background = '#FFBFBD')
        self.root.geometry("1200x600")
        self.root.resizable(True, True)
        self.root.maxsize(width = 1300, height = 700)
        self.root.minsize(width = 1100, height = 500)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = "#FFF7EF", 
                             highlightbackground = "#FFA78B", highlightthickness = 3)
        self.frame_1.place(relx = 0.01 , rely = 0.01, relwidth = 0.98, relheight = 0.46)
        
        self.frame_2 = Frame(self.root, bd = 4, bg = "#FFF7EF", 
                             highlightbackground = "#FFA78B", highlightthickness = 3)
        self.frame_2.place(relx = 0.01 , rely = 0.5, relwidth = 0.98, relheight = 0.46)
    
    def criando_botoes(self):
        #criação do botão de limpar
        self.bt_limpar = Button(self.frame_1, text = "Limpar")
        self.bt_limpar.place(relx = 0.2 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )

         #criação do botão de Buscar
        self.bt_limpar = Button(self.frame_1, text = "Buscar")
        self.bt_limpar.place(relx = 0.31 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )

        #criação do botão de Novo
        self.bt_limpar = Button(self.frame_1, text = "Novo")
        self.bt_limpar.place(relx = 0.42 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )

        #criação do botão de Alterar
        self.bt_limpar = Button(self.frame_1, text = "Alterar")
        self.bt_limpar.place(relx = 0.53 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )

        #criação do botão de Apagar
        self.bt_limpar = Button(self.frame_1, text = "Apagar")
        self.bt_limpar.place(relx = 0.64 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )



application()









