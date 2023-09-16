# xThemis
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Banco


def popular():
    tv.delete(*tv.get_children())
    vQuery = "SELECT * FROM Agenda order by N_IDCONTATO"
    linhas = Banco.dql(vQuery)
    for i in linhas:
        tv.insert("", "end", values=i)


def inserir():
    if vnome.get() == "" or vfone.get() == "" or vemail.get() == "":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    try:
        vQuery = f"INSERT INTO Agenda (T_NOMECONTATO,T_TELCONTATO,T_EMAILCONTATO) VALUES ('{vnome.get()}','{vfone.get()}','{vemail.get()}')"
        Banco.dml(vQuery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao inserir")
        return
    vnome.delete(0, END)
    vfone.delete(0, END)
    vemail.delete(0, END)
    vnome.focus()


def deletar():
    try:
        vid = -1
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        vid = valores[0]
        vQuery = f"DELETE FROM Agenda WHERE N_IDCONTATO={vid}"
        Banco.dml(vQuery)
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Apenas selecione o contato")
        return


def pesquisar():
    tv.delete(*tv.get_children())
    vQuery = f"SELECT * FROM Agenda WHERE T_NOMECONTATO LIKE '%{vnPesquisar.get()}%' order by N_IDCONTATO"
    linhas = Banco.dql(vQuery)
    for i in linhas:
        tv.insert("", "end", values=i)


App = Tk()
App.title("Banco de Dados")
App.geometry("650x450")
App.configure(background="#088")

quadroGrid = LabelFrame(App, text="Contatos", background="#088", fg="#fff", font=12)
quadroGrid.pack(fill="both", expand=YES, padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=("id", "nome", "fone", "email"), show="headings")
tv.column("id", minwidth=1, width=30)
tv.column("nome", minwidth=1, width=150)
tv.column("fone", minwidth=1, width=100)
tv.column("email", minwidth=1, width=180)
tv.heading("id", text="ID")
tv.heading("nome", text="NOME")
tv.heading("fone", text="TELEFONE")
tv.heading("email", text="EMAIL")
tv.pack()
popular()

quadroInserir = LabelFrame(
    App, text="Inserir Novos Contatos", background="#088", fg="#fff", font=12
)
quadroInserir.pack(fill="both", expand=YES, padx=10, pady=10)

lbnome = Label(quadroInserir, text="Nome")
lbnome.pack(side="left")
vnome = Entry(quadroInserir)
vnome.pack(side="left", padx=10)

lbfone = Label(quadroInserir, text="Telefone")
lbfone.pack(side="left", padx=5)
vfone = Entry(quadroInserir)
vfone.pack(side="left", padx=5)

lbemail = Label(quadroInserir, text="Email")
lbemail.pack(side="left", padx=5)
vemail = Entry(quadroInserir)
vemail.pack(side="left", padx=5)

btn_inserir = Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side="left", padx=5)


quadroPesquisar = LabelFrame(
    App, text="Pesquisar", background="#088", fg="#fff", font=12
)
quadroPesquisar.pack(fill="both", expand=YES, padx=10, pady=10)

lbid = Label(quadroPesquisar, text="Nome")
lbid.pack(side="left")
vnPesquisar = Entry(quadroPesquisar)
vnPesquisar.pack(side="left", padx=10)
btn_Pesquisar = Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_Pesquisar.pack(side="left", padx=10)
btn_todos = Button(quadroPesquisar, text="Mostrar Todos", command=popular)
btn_todos.pack(side="left", padx=10)
btn_deletar = Button(quadroPesquisar, text="Deletar", command=deletar)
btn_deletar.pack(side="left", padx=10)

App.mainloop()
