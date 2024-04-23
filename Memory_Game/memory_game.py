import tkinter as tk
from tkinter import messagebox
import random

"TKINTER: Biblioteca do python para interfaces gráficas"

"Definindo configurações do jogo"
num_linhas = 4
num_colunas = 4
cartao_largura = 10
cartao_altura = 5
cartao_cores = ['red','blue','green','yellow','purple','orange','cyan','pink']
fundo_cor = '#4F4F4F'
letra_cor = '#ffffff'
font_style = ('Arial',12,'bold')
maximo_de_tentantivas = 25

#Criando a interface principal

janela = tk.Tk() # cria a janela que será aberta quando o game rodar 
janela.title('Memory Game')
janela.configure(bg=fundo_cor)#Atribui configurações a sua janela dando valores a atributos bg (back ground, recebe a cor do fundo a cor da janela)


#Criando uma grade aleatoria de cores para os cartões
def criar_cartao_grid():
    cores = cartao_cores * 2 #apenas dois cartões de cada cor
    random.shuffle(cores)# shuffle: embaralha os elementos da lista
    grid = []

    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid



#criando grade de cartoes
grid = criar_cartao_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes = []
numero_tentativas = 0


for linha in range(num_linhas):
    linha_de_cartoes = []
    for coluna in range(num_colunas):
        cartao = tk.Button(janela,command= lambda r= linha, c = coluna:cartao_clicado(r,c), width=cartao_largura,height=cartao_altura,bg= 'black',relief=tk.RAISED,bd=3)
        cartao.grid(row=linha, column= coluna,padx=5,pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)

# Personalizando os botoes (como todos os botões terão o mesmo estilo vamos atribuir todos as caracteristicas dos botoes num dicionário)
button_style = {'activebackground': '#f8f9fa', 'font': font_style, 'fg': letra_cor}
janela.option_add('*Button',button_style)#adicionando botão na janela 



#Rótulo com o número de tentativas 
rotulo_tentativas = tk.Label(janela, text= 'tentativas: {}/{}'.format(numero_tentativas,maximo_de_tentantivas, fg= letra_cor, bg= fundo_cor, font= font_style))#cria um rótulo
rotulo_tentativas.grid(row=num_linhas,columnspan=num_colunas,padx=10, pady=10)#posiciona o rotulo no grid(pad x (afastamento horizontal e pady afantasmento vertical))


# evento de clickar no cartao
def cartao_clicado(linha,coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()


#verificar se as cores dos cartoes são iguais
def check_match():
    cartao1,cartao2 = cartao_revelado
    if cartao1['bg'] == cartao2['bg']:
        cartao1.after(1000,cartao1.destroy)
        cartao2.after(1000,cartao2.destroy)
        cartao_correspondentes.extend([cartao1,cartao2])
        check_win()
    else:
       cartao1.after(1000,lambda:cartao1.config(bg='black')) 
       cartao2.after(1000,lambda:cartao2.config(bg='black'))
    cartao_revelado.clear()
    update_score()


#verificar se o jogador ganhou 
def check_win():
    if len(cartao_correspondentes) == num_linhas * num_colunas:
        messagebox.showinfo('Parabéns!', 'Você ganhou o jogo!')
        janela.quit()


#Atualiza a pontuação dos acertos e verificar se o jogador perdeu o jogo
def update_score():
    global numero_tentativas
    numero_tentativas  += 1
    rotulo_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas,maximo_de_tentantivas))
    if numero_tentativas >= maximo_de_tentantivas:
        messagebox.showinfo('Fim de jogo','Você perdeu')
        janela.quit()








janela.mainloop()#cria o loop principal do jogo, faz a janela ficar rodando e o game rodar 




