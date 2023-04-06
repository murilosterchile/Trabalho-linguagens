"""
Trabalho final - Linguagens Formais e Autômatos

grupo:
    - Murilo Sterchile
    - Arthur Sauer
    - Luca Boni

"""
#   biblioteca que permite executa uma tarefa em um intervalo de tempo pré-determinado.
import time

#   Gramática é um arquivo em python que foi criado para definir as seguintes partes do trabalho:Alfabeto, transições,
#estado final e estado inicial. Todas essas definições foram importados para a main, para permitir a execução do código.
from gramatica import alfabeto, estado_inicial, estado_final, transições


#   Função que implementa o autômato, recebe como entrada uma palavra(string), e processa essa palavra da seguinte maneira:
#primeiro é atribuído o estado atual como q0(estado inicial) e após isso irá percorrer a palavra e verificar se ela
#a linguagem.
def automato(input_string):
    # Inicialização do estado atual
    estado_atual = estado_inicial

    numero_interacao = 0

    # Laço para percorrer a entrada
    for symbol in input_string:

        numero_interacao = numero_interacao + 1

        # Verificação se o símbolo pertence ao alfabeto
        if symbol not in alfabeto:
            return print(f'símbolo ({symbol}) não pertence ao alfabeto')

        # Verificação se há uma regra de transição para o símbolo e estado atual
        if (estado_atual, symbol) not in transições:
            return print(f'transição ({estado_atual},{symbol}) não existe')

        time.sleep(0.3)
        print(f'{numero_interacao}º interação({estado_atual},{symbol}) -> {transições[(estado_atual, symbol)]}')

        # Atualização do estado atual
        estado_atual = transições[(estado_atual, symbol)]

    # Verificação se o estado atual é um estado final
    return estado_atual in estado_final

#   A função ler_entrada irá ler a palavra inserida manualmente pelo usuário, caso opte com interagir desse modo
def ler_entrada():
    input_string = input("Informe a palavra: ")
    return input_string

#   A função ler_arquivo ira ler o arquivo com as interações fornecidas pelo usuário, esse arquivo deve ser do tipo .txt
#e deverá ser informado o seu caminho, como pro exemplo: C:\Users\muril\Downloads\caso1.txt, onde o arquivo está na
#pasta Downloads do usuário.
def ler_arquivo(caminho):
    with open(caminho, "r") as file:
        input_string = file.read().replace('\n', '')
    return input_string

#   Essa parte do código é a implementação do programa, em que o usuário poderá fazer quantas operações quiser. Para isso
#basta responder 's' quando o programa perguntar se deseja mais uma operação, caso contrario o programa encerra.
while True:
    # Verificação se foi passado um arquivo de texto como argumento
    caminho = input("Informe o caminho do arquivo ou pressione enter para informar a palavra manualmente: ")

    if caminho:
        input_string = ler_arquivo(caminho)
    else:
        input_string = ler_entrada()

    j = automato(input_string)

    if j == True:
        print("palavra aceita\n")
    else:
        print("palavra rejeitada\n")

    k = input('deseja realizar mais uma operação: (s) sim ou (n) não \n')

    if k == "n":
        break
