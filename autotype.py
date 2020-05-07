import keyboard

a_file = open("texto.txt", "r")

lista = [line.strip() for line in a_file]

a_file.close()

i = 0
last = lista.__len__() - 1

def escrever():
    global i
    if i <= last:
        # lista[i]
        keyboard.write(lista[i], 0.05)
        i += 1

def voltar():
    global i
    if i > 0:
        i -= 1

def avancar():
    global i
    if i < last:
        i += 1

def zerar():
    global i
    i = 0

keyboard.add_hotkey('F8', escrever)
keyboard.add_hotkey('F7', voltar)
keyboard.add_hotkey('F10', lambda: avancar())
keyboard.add_hotkey('F9', lambda: zerar())

keyboard.wait('esc')