import keyboard

lista = []
linha_atual = 0
total_linhas = 0

def carregarLista():
    global lista, linha_atual, total_linhas
    linha_atual = 0
    lista = []
    arquivo_texto = open("texto.txt", "r", encoding="utf-8")
    for linha in arquivo_texto:
        lista.append(linha.replace('\n', ''))
    arquivo_texto.close()
    total_linhas = lista.__len__() - 1

def escrever():
    global linha_atual
    velocidade_digitacao = 0.05
    if linha_atual <= total_linhas:
        if lista[linha_atual][:2] == '##':
            keyboard.press(lista[linha_atual][2:])
        else:
            keyboard.write(lista[linha_atual], velocidade_digitacao)

        linha_atual += 1

        while linha_atual <= total_linhas and lista[linha_atual][:2] == '##':
            if lista[linha_atual][2:3] == ' ':
                keyboard.write(lista[linha_atual][3:], velocidade_digitacao)
            else:
                keyboard.press(lista[linha_atual][2:])
            linha_atual += 1


def voltar():
    global linha_atual
    if linha_atual > 0:
        linha_atual -= 1

def avancar():
    global linha_atual
    if linha_atual < total_linhas:
        linha_atual += 1

def zerar():
    global linha_atual
    linha_atual = 0

carregarLista()
keyboard.add_hotkey('F6', carregarLista)
keyboard.add_hotkey('F7', voltar)
keyboard.add_hotkey('F8', escrever)
keyboard.add_hotkey('F9', zerar)
keyboard.add_hotkey('F10', avancar)

keyboard.wait('esc')