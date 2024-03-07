import tkinter as tk
import copy
#criando a janela principal
root = tk.Tk()
root.geometry("720x480")
#escolhendo o lado
## função de escolha do lado
player = 1
ia = 0
#definindo o estado inicial do tabuleiro
tabuleiro = []
dicio = {}
for i in range(1,4):
    linha = []
    for j in range(1,4):
        linha.append("")
    tabuleiro.append(linha)
#variavel do vencedor
def fim_de_jogo(tabuleiro):
    if(tabuleiro[0][0] == tabuleiro[0][1] and tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != ''):
        return (True,tabuleiro[0][0])
    elif(tabuleiro[1][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[1][2]and tabuleiro[1][1] != ''):
        return (True,tabuleiro[1][0])
    elif(tabuleiro[2][0] == tabuleiro[2][1] and tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][1] != ''):
        return (True,tabuleiro[2][0])
    elif(tabuleiro[0][0] == tabuleiro[1][0] and tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[1][0] != ''):
        return (True,tabuleiro[0][0])
    elif(tabuleiro[0][1] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[1][1] != ''):
        return (True,tabuleiro[0][1])
    elif(tabuleiro[0][2] == tabuleiro[1][2] and tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[1][2] != ''):
        return (True,tabuleiro[0][2])
    elif(tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[1][1] != ''):
        return (True,tabuleiro[0][0])
    elif(tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[2][0] != ''):
        return (True,tabuleiro[0][2])
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == ''):
                return (False,'')
    return (True,'')
def jogador0():
      global player
      global ia
      player = 0
      ia = 1
def jogadorx():
      global player
      global ia
      player = 1
      ia = 0  
def on_click(a,b):
    global tabuleiro
    global player
    global dicio
    global lb
    if(tabuleiro[a-1][b-1] == ""):
        botao = dicio[f"grade{a}{b}"]
        if(player == 1):
            botao.config(text="X")
            tabuleiro[a-1][b-1] = "X"
        else:
            botao.config(text="O")
            tabuleiro[a-1][b-1] = "O"
        (final,vencedor) = fim_de_jogo(tabuleiro)
        if(final and vencedor != ''):
            lb = tk.Label(text=f"Fim de jogo, o vencedor foi {vencedor}")
            lb.place(x=280,y=120)
            return
        elif(final and vencedor == ''):
            lb = tk.Label(root,text="Empate")
            lb.place(x=280,y=120)
            return
        x,y = decide_movimento(tabuleiro)
        #print(f"{x},{y}")
        botaoia = dicio[f"grade{x+1}{y+1}"]
        if(ia == 1):
            botaoia.config(text="X")
            tabuleiro[x][y] = "X"
        else:
            botaoia.config(text="O")
            tabuleiro[x][y] = "O"
        (final,vencedor) = fim_de_jogo(tabuleiro)

        if(final and vencedor != ''):
            lb = tk.Label(text=f"Fim de jogo, o vencedor foi {vencedor}")
            lb.place(x=280,y=120)
            return
        elif(final and vencedor == ''):
            lb = tk.Label(root,text="Empate")
            lb.place(x=280,y=120)
            return
    else:
        pass
def valor_jogada(tabuleiro,ia):
    soma_x_c_ia = [0,0,0]
    soma_O_c_ia = [0,0,0]
    soma_X_c_player = [0,0,0]
    soma_O_c_player = [0,0,0]
    soma_linha_vazia = [0,0,0]
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] != ''):
                soma_linha_vazia[i] += 1
            if(tabuleiro[i][j] == 'X'):
                if(ia == 1):
                    soma_x_c_ia[i] += 1
                else:
                    soma_X_c_player[i] += 1
            if(tabuleiro[i][j] == 'O'):
                if(ia == 0):
                    soma_O_c_ia[i] += 1
                else:
                    soma_O_c_player[i] += 1
    if(max(soma_x_c_ia) == 3):
        return float('+inf')
    if(max(soma_X_c_player) == 3):
        return float('-inf')
    if(max(soma_O_c_ia) == 3):
        return float('+inf')
    if(max(soma_O_c_player) == 3):
        return float('-inf')
    #definindo as variaveis de coluna
    soma_X_L_ia = [0,0,0]
    soma_O_L_ia = [0,0,0]
    soma_X_L_player = [0,0,0]
    soma_O_L_player = [0,0,0]
    soma_coluna_vazia = [0,0,0]
    valor_da_coluna = 0
    for j in range(3):
        for i in range(3):
            if(tabuleiro[i][j] != ''):
                soma_coluna_vazia[j] += 1
            if(tabuleiro[i][j] == 'X'):
                if(ia == 1):
                    soma_X_L_ia[j] += 1
                else:
                    soma_X_L_player[j] += 1
            if(tabuleiro[i][j] == 'O'):
                if(ia == 0):
                    soma_O_L_ia[j] += 1
                else:
                    soma_O_L_player[j] += 1
    soma_X_dia_ia = [0,0]
    soma_O_dia_ia = [0,0]
    soma_X_dia_player = [0,0]
    soma_O_dia_player = [0,0]
    soma_dia_vazia = [0,0]
    for i in range(3):
        if tabuleiro[i][i] == "X":
            if(ia == 1):
                soma_X_dia_ia[0] += 1
            else:
                soma_X_dia_player[0] += 1
        elif (tabuleiro[i][i]) == "O":
            if(ia == 0):
                soma_O_dia_ia[0] += 1
            else:
                soma_O_dia_player[0] += 1
        elif(tabuleiro[i][i] == ''):
            soma_dia_vazia[0] += 1
    if(max(soma_X_L_ia) == 3):
        return float('+inf')
    if(max(soma_X_L_player) == 3):
        return float('-inf')
    if(max(soma_O_L_ia) == 3):
        return float('+inf')
    if(max(soma_O_L_player) == 3):
        return float('-inf')
    for i in range(3):
        if tabuleiro[i][2-i] == "X":
            if(ia == 1):
                soma_X_dia_ia[1] += 1
            else:
                soma_X_dia_player[1] += 1
        elif (tabuleiro[i][2-i]) == "O":
            if(ia == 0):
                soma_O_dia_ia[1] += 1
            else:
                soma_O_dia_player[1] += 1
        elif(tabuleiro[i][2-i] == ''):
            soma_dia_vazia[1] += 1
    #verifica se ja houve vencedor


    if(max(soma_X_dia_ia) == 3):
        return float('+inf')
    if(max(soma_X_dia_player) == 3):
        return float('-inf')
    if(max(soma_O_dia_ia) == 3):
        return float('+inf')
    if(max(soma_O_dia_player) == 3):
        return float('-inf')
    #soma total do tabuleiro
    valor_jogada = 0
    #print(soma_O_c_ia)
    for i in range(3):
        #checando linhas
        if (soma_x_c_ia[i] != 0  and soma_O_c_player[i] == 0) :
            valor_jogada += 10**(soma_x_c_ia[i]-1)
        if soma_x_c_ia[i] == 0  and soma_O_c_player[i] != 0:
            valor_jogada -= 10**(soma_O_c_player[i] - 1)
            if(soma_O_c_player == 3):
                return float('-inf')
        #checando colunas
        if (soma_X_L_ia[i] != 0  and soma_O_L_player[i] == 0) :
            valor_jogada += 10**(soma_X_L_ia[i]-1)
        if soma_x_c_ia[i] == 0  and soma_O_L_player[i] != 0:
            valor_jogada -= 10**(soma_O_L_player[i] - 1)
    #checando diagonal principal
    if soma_X_dia_ia[0] != 0  and soma_O_c_player[0] == 0:
        valor_jogada += 10**(soma_O_dia_ia[0] - 1)
    if soma_X_dia_ia[0] == 0  and soma_O_c_player[0] != 0:
        valor_jogada -= 10**(soma_O_dia_player[0] - 1)
    #checando diagonal secundaria
    if soma_X_dia_ia[1] != 0  and soma_O_c_player[1] == 0:
        valor_jogada += 10**(soma_O_dia_ia[0] - 1)
    if soma_X_dia_ia[1] == 0  and soma_O_c_player[1] != 0:
        valor_jogada -= 10**(soma_O_dia_player[0] - 1)    
    return valor_jogada
def valor_jogada1(vencedor, ia):
    if (vencedor == "X" and ia == 1):
        return 1
    elif(vencedor == "O" and ia == 1):
        return -1
    elif(vencedor == "X" and ia == 0):
        return -1
    elif(vencedor == "O" and ia == 0):
        return 1
    else:
        return 0
def minmax(tabuleiro,profundidade,alpha,beta,maximizando):
    global ia
    fim,vencedor = fim_de_jogo(tabuleiro)
    if(fim):
        return valor_jogada1(vencedor,ia)
    if (maximizando):
        maior_valor = float('-inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == '':
                    tabuleiro_temp = copy.deepcopy(tabuleiro)
                    if(ia == 1):
                        tabuleiro_temp[i][j] = "X"
                    else:
                        tabuleiro_temp[i][j] = "O"
                    
                    valor = minmax(tabuleiro_temp,profundidade - 1,alpha,beta,False)
                   
                    maior_valor = max(valor,maior_valor)
                    alpha = max(alpha,valor)
                    if beta <= alpha:
                        break
        return maior_valor
    else:
        menor_valor = float('+inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == '':
                    tabuleiro_temp = copy.deepcopy(tabuleiro)
                    if(player == 1):
                        tabuleiro_temp[i][j] = "X"
                    else:
                        tabuleiro_temp[i][j] = "O"
                    
                    valor = minmax(tabuleiro_temp,profundidade - 1,alpha,beta,True)
                    menor_valor= min(valor,menor_valor)
                    beta = min(valor,beta)
                    if beta <= alpha:
                        break
        return menor_valor
def decide_movimento(tabuleiro):
    global ia
    melhor_valor = float('-inf')
    proxima_jogada = None
    for i in range(3):
        for j in range(3):
           if(tabuleiro[i][j] == '') :
                tabuleiro_temp = copy.deepcopy(tabuleiro)
                if(ia == 1):
                    tabuleiro_temp[i][j] = "X"
                else:
                    tabuleiro_temp[i][j] = "O"
                valor = minmax(tabuleiro_temp,6,float('-inf'),float('+inf'),False)
                #print(valor)
                if(melhor_valor <= valor):
                    melhor_valor = valor
                    proxima_jogada = (i,j)
    return proxima_jogada
def reset():
    global tabuleiro
    global dicio
    global lb
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = ""
            botao = dicio[f"grade{i+1}{j+1}"]
            botao.config(text="")
            lb.config(text="")
            
#função para criar a interface do jogo
def inicializar_interface():
    global dicio
    button_x = tk.Button(root,height=3,width=10,text="Jogar como X",command=jogadorx)
    button_x.place(x= 250,y=40)
    button_o = tk.Button(root,height=3,width=10,text="Jogar como O",command=jogador0)
    button_o.place(x=360,y=40)
    button_clr = tk.Button(root, height=3, width=10, text="Reiniciar", command=reset)
    button_clr.place(x=470,y=40)
    #label
    label1 = tk.Label(root,text="Jogo da velha")
    label1.place(x=310,y= 10)
    posy = 150
    for i in range(1, 4):
        posx = 270
        for j in range(1, 4):
            gradeij = tk.Button(root, height=3, width=4, command=lambda a=i, b=j: on_click(a, b))
            gradeij.place(x=posx, y=posy)
            dicio[f"grade{i}{j}"] = gradeij
            posx += 60
        posy += 70
    return 1
if(inicializar_interface()):
     print("inicializado com sucesso")
root.mainloop()

