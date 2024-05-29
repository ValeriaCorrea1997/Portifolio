import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

#------------------------funções--------------------------#
def cor():
    color = colorchooser.askcolor(title="escolha uma cor")[1]
    areadetexto.config(fg=color)
    fonte_cor = font.Font(areadetexto, areadetexto.cget("font"))
    areadetexto.tag_configure("cororido", font=fonte_cor, foreground=color)

    current_tags = areadetexto.tag_names("sel.first")

    if "cororido" in current_tags:
        areadetexto.tag_remove("cororido", "sel.first", "sel.last")
    else:
        areadetexto.tag_add("cororido", "sel.first", "sel.last")

def fonte(*args):
    areadetexto.config(font=(font_name.get(), mudar_tamanho.get()))

def novo():
    window.title("Documento Sem Nome")
    areadetexto.delete(1.0,END)

def abrir():
    file = askopenfilename(defaultextension=".txt", file=[("All Files","*.*"),("Text Documents",".txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            areadetexto.delete(1.0,END)
            file = open(file, "r")
            areadetexto.insert(1.0,file.read)
        except Exception:
            messagebox.showwarming(title="Erro!", Message="Não foi possível abrir o arquivo")

def salvar():
    file = filedialog.asksaveasfilename(initialfile="Documento Sem Nome", defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

def fechar():
    window.destroy()

def copiar():
    areadetexto.event_generate("<<Copy>>")

def colar():
    areadetexto.event_generate("<<Paste>>")

def cortar():
    areadetexto.event_generate("<<Cut>>")

def negrito ():
    fonte_negrito = font.Font(areadetexto, areadetexto.cget("font"))
    fonte_negrito.configure(weight="bold")
    areadetexto.tag_configure("bold", font=fonte_negrito)

    current_tags = areadetexto.tag_names("sel.first")

    if "bold" in current_tags:
        areadetexto.tag_remove("bold", "sel.first", "sel.last")
    else:
        areadetexto.tag_add("bold", "sel.first", "sel.last")
    
def italico ():
    fonte_italico = font.Font(areadetexto, areadetexto.cget("font"))
    fonte_italico.configure(slant="italic")
    areadetexto.tag_configure("italic", font=fonte_italico)

    current_tags = areadetexto.tag_names("sel.first")

    if "italic" in current_tags:
        areadetexto.tag_remove("italic", "sel.first", "sel.last")
    else:
        areadetexto.tag_add("italic", "sel.first", "sel.last")


def sublinhado ():
    areadetexto.config(font=(font_name.get(), font_size.get(), 'underline'))

def escuro ():
    window.config(bg="grey21")
    areadetexto.config(bg="grey21", fg="silver")

#------------------------janela--------------------------#
window = Tk()
window.title("Criador de Notas")
file = None

#------------------centralizar janela--------------------#
window_width = 808
window_height = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#------------------------menus--------------------------#
barra_de_menu = Menu(window)
window.config(menu=barra_de_menu)

menu_arquivo = Menu(barra_de_menu, tearoff=0)
barra_de_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo             Crtl+N", command=novo)
menu_arquivo.add_command(label="Abrir              Crtl+O", command=abrir)
menu_arquivo.add_command(label="Salvar            Crtl+S", command=salvar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Fechar Programa  X", command=fechar)

menu_editar = Menu(barra_de_menu, tearoff=0)
barra_de_menu.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Copiar             Crtl+C", command=copiar)
menu_editar.add_command(label="Colar               Crtl+V", command=colar)
menu_editar.add_command(label="Recortar          Crtl+X", command=cortar)

#------------------barra de ferramentas------------------#
font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("20")

barra_de_ferramentas = Frame(window, bg="CornflowerBlue", padx=7, pady=7)
barra_de_ferramentas.grid(stick=W)

botaocor = Button(barra_de_ferramentas, text="Cor do Texto", font=("Ink Free",12), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=cor, padx=20, pady=5)
botaocor.grid(row=0, column=0)

botaofonte = Button(barra_de_ferramentas, text="Fonte", font=("Ink Free",12), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=fonte, padx=2, pady=5)
botaofonte.grid(row=0, column=1)

mudar_fonte = OptionMenu(barra_de_ferramentas, font_name, *font.families(), command=fonte)
mudar_fonte.grid(row=0, column=2)

botaotamanho = Button(barra_de_ferramentas, text="Tamanho da Fonte", font=("Ink Free",12), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=fonte, padx=10, pady=5)
botaotamanho.grid(row=0, column=3)

mudar_tamanho = Spinbox(barra_de_ferramentas, from_=1, to=100, textvariable=font_size, command=fonte)
mudar_tamanho.grid(row=0, column=4)

negrito = Button(barra_de_ferramentas, text="N", font=("Arial", 12, 'bold'), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=negrito, padx=10, pady=5)
negrito.grid(row=0, column=5)

italico = Button(barra_de_ferramentas, text="I", font=("Arial", 12, 'italic'), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=italico, padx=10, pady=5)
italico.grid(row=0, column=6)

sublinhado = Button(barra_de_ferramentas, text="S", font=("Arial", 12, 'underline'), bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=sublinhado, padx=10, pady=5)
sublinhado.grid(row=0, column=7)

tema_escuro = Button(barra_de_ferramentas, text="Tema Escuro", font=("Ink Free",12),bg="CornflowerBlue", relief=SOLID, borderwidth=0, command=escuro, padx=22, pady=5)
tema_escuro.grid(row=0, column=8)

#--------------------área de texto-----------------------#
areadetexto = Text(window, font=(font_name.get(), font_size.get()), height=59, width=100)
areadetexto.grid(sticky=N + E + S + W)

#----------------------scroll bar------------------------#
scroll_bar = Scrollbar(areadetexto)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
areadetexto.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
areadetexto.config(yscrollcommand=scroll_bar.set)

#--------------------inicia a janela---------------------#
window.mainloop()