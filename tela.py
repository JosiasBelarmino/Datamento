from tkinter import *
from tkinter import ttk
root = Tk()

class application():
    def __init__ (self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        root.mainloop()
    def tela(self):
        self.root.title("Datamento")
        self.root.configure(background = '#4E8397')
        self.root.geometry("1200x600")
        self.root.resizable(True, True)
        self.root.maxsize(width = 1300, height = 700)
        self.root.minsize(width = 1100, height = 500)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = "#FFF7EF", 
                             highlightbackground = "#83B8CD", highlightthickness = 3)
        self.frame_1.place(relx = 0.01 , rely = 0.01, relwidth = 0.98, relheight = 0.46)
        
        self.frame_2 = Frame(self.root, bd = 4, bg = "#FFF7EF", 
                             highlightbackground = "#83B8CD", highlightthickness = 3)
        self.frame_2.place(relx = 0.01 , rely = 0.5, relwidth = 0.98, relheight = 0.46)
    
    def widgets_frame_1(self):
        #criação do botão de limpar
        self.bt_limpar = Button(self.frame_1, text = "Limpar", bd = 1, bg = "#547EA0", fg = "white",
                                font = ("verdana", 9, "bold"))
        self.bt_limpar.place(relx = 0.2 , rely = 0.1, relwidth= 0.1, relheight= 0.15 )

         #criação do botão de Buscar
        self.bt_buscar = Button(self.frame_1, text = "Buscar",bd = 1, bg = "#547EA0", fg = "white",
                                font = ("verdana", 9, "bold"))
        self.bt_buscar.place(relx = 0.31 , rely = 0.1, relwidth = 0.1, relheight = 0.15 )

        #criação do botão de Novo
        self.bt_novo = Button(self.frame_1, text = "Novo",bd = 1, bg = "#547EA0", fg = "white",
                                font = ("verdana", 9, "bold"))
        self.bt_novo.place(relx = 0.42 , rely = 0.1, relwidth = 0.1, relheight = 0.15 )

        #criação do botão de Alterar
        self.bt_alterar = Button(self.frame_1, text = "Alterar",bd = 1, bg = "#547EA0", fg = "white",
                                font = ("verdana", 9, "bold"))
        self.bt_alterar.place(relx = 0.53 , rely = 0.1, relwidth = 0.1, relheight = 0.15 )

        #criação do botão de Apagar
        self.bt_apagar = Button(self.frame_1, text = "Apagar",bd = 1, bg = "#547EA0", fg = "white",
                                font = ("verdana", 9, "bold"))
        self.bt_apagar.place(relx = 0.64 , rely = 0.1, relwidth = 0.1, relheight = 0.15 )

        #Criação da lapel e entrada do Codigo
        self.lb_codigo = Label(self.frame_1, text = "Código", fg = "#4E8397", font = ("verdana", 9, "bold"))
        self.lb_codigo.place(relx = 0.02 , rely = 0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.02 , rely = 0.15, relheight =0.1 , relwidth = 0.15)

        #Criação da lapel e entrada do Nome
        self.lb_nome = Label(self.frame_1, text = "Nome", fg = "#4E8397", font = ("verdana", 9, "bold"))
        self.lb_nome.place(relx = 0.02 , rely = 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.02 , rely = 0.45, relheight = 0.1 , relwidth = 0.88)

        #Criação da lapel e entrada do Telefone
        self.lb_telefone = Label(self.frame_1, text = "Telefone", fg = "#4E8397", font = ("verdana", 9, "bold"))
        self.lb_telefone.place(relx = 0.02 , rely = 0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx = 0.02 , rely = 0.7, relheight =0.1 , relwidth = 0.4)

        #Criação da lapel e entrada do Cidade
        self.lb_cidade = Label(self.frame_1, text = "Cidade", fg = "#4E8397", font = ("verdana", 9, "bold"))
        self.lb_cidade.place(relx = 0.5 , rely = 0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx = 0.5 , rely = 0.7, relheight =0.1 , relwidth = 0.4)

    def lista_frame_2(self):
        #Definindo quantidade de colunas
        self.listaCli = ttk.Treeview(self.frame_2, height = 3, column = ("col1", "col2", "col3", "col4"))
       
        #Nomeando Colunas definidas
        self.listaCli.heading("#0", text = "")
        self.listaCli.heading("#1", text = "Código")
        self.listaCli.heading("#2", text = "Nome")
        self.listaCli.heading("#3", text = "Telefone")
        self.listaCli.heading("#4", text = "Cidade")

        #Tamanho das colunas, lembrando que a coluna 0 tem que ser declarada mas não aparece
        self.listaCli.column("#0", width = 0)
        self.listaCli.column("#2", width = 200)
        self.listaCli.column("#3", width = 125)
        self.listaCli.column("#4", width = 125)

        #Declaração posições da lista
        self.listaCli.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.85)

        #barra de rolagem
        #Posição
        self.scroolLista = Scrollbar(self.frame_2, orient = "vertical")
        #A quem a barra percente (esta vinculada)
        self.listaCli.configure(yscroll = self.scroolLista.set)
        #Onde ela fica
        self.scroolLista.place(relx = 0.96, rely = 0.1, relwidth = 0.04, relheight = 0.85)




application()









