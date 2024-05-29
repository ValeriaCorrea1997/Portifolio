from tkinter import *
import random

def proximo(row, column):

    global player

    if botoes[row][column]['text'] == "" and vencedor() is False:

        if player == players[0]:

            botoes[row][column]['text'] = player

            if vencedor() is False:
                player = players[1]
                label.config(text=("vez de "+players[1]))

            elif vencedor() is True:
                label.config(text=(players[0]+" venceu o jogo"))

            elif vencedor() == "Empate":
                label.config(text="Empate!")

        else:

            botoes[row][column]['text'] = player

            if vencedor() is False:
                player = players[0]
                label.config(text=("vez de " +players[0]))

            elif vencedor() is True:
                label.config(text=(players[1]+" venceu o jogo"))

            elif vencedor() == "Empate":
                label.config(text="Empate!")

def vencedor():

    for row in range(3):
        if botoes[row][0]['text'] == botoes[row][1]['text'] == botoes[row][2]['text'] != "":
           botoes[row][0].config(bg="#3cb371")
           botoes[row][1].config(bg="#3cb371")
           botoes[row][2].config(bg="#3cb371")
           return True

    for column in range(3):
        if botoes[0][column]['text'] == botoes[1][column]['text'] == botoes[2][column]['text'] != "":
           botoes[0][column].config(bg="#3cb371")
           botoes[1][column].config(bg="#3cb371")
           botoes[2][column].config(bg="#3cb371")
           return True

    if botoes[0][0]['text'] == botoes[1][1]['text'] == botoes[2][2]['text'] != "":
       botoes[0][0].config(bg="#3cb371")
       botoes[1][1].config(bg="#3cb371")
       botoes[2][2].config(bg="#3cb371")
       return True

    elif botoes[0][2]['text'] == botoes[1][1]['text'] == botoes[2][0]['text'] != "":
         botoes[0][2].config(bg="#3cb371")
         botoes[1][1].config(bg="#3cb371")
         botoes[2][0].config(bg="#3cb371")
         return True

    elif espacos_vazios() is False:

        for row in range(3):
            for column in range(3):
                botoes[row][column].config(bg="khaki")
        return "Empate"

    else:
        return False


def espacos_vazios():

    casas = 9

    for row in range(3):
        for column in range(3):
            if botoes[row][column]['text'] != "":
                casas -= 1

    if casas == 0:
        return False
    else:
        return True

def novo_jogo():

    global player

    player = random.choice(players)

    label.config(text="vez de "+player)

    for row in range(3):
        for column in range(3):
            botoes[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Jogo da velha")
window.geometry("1000x800")
players = ["X","O"]
player = random.choice(players)
botoes = [[0,0,0],
          [0,0,0],
          [0,0,0]]

label = Label(window, text="Jogo da Velha", font=("Berlin Sans FB Demi", 70), fg="#6495ed")
label.pack(side="top")

label = Label(text="Vez de "+player, font=('Arial Rounded MT Bold',40))
label.pack(side="top")


frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        botoes[row][column] = Button(frame, text="",font=('Arial Rounded MT Bold',40), relief=RAISED, bd=10, width=5, height=2,
                                      command= lambda row=row, column=column: proximo(row,column))
        botoes[row][column].grid(row=row,column=column)

jogar_novamente = Button(text="Jogar Novamente", font=('Arial Rounded MT Bold',20), relief=SOLID, bd=0, pady=10, command=novo_jogo)
jogar_novamente.pack(side="top")


window.mainloop()