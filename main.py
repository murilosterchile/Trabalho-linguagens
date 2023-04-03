"""
Trabalho final - Linguagens Formais e Autômatos

grupo:
    - Murilo Sterchile dos Santos
    - Arthur Sauer
    - Luca bonni

"""

from gramatica import alfabeto, estado_inicial, estado_final, transições
# C:\Users\muril\Downloads\caso1.txt  -> exemplo de caminho para arquivo
def automato(input_string):
    # Inicialização do estado atual
    estado_atual = estado_inicial

    # Laço para percorrer a entrada
    for symbol in input_string:
        # Verificação se o símbolo pertence ao alfabeto
        if symbol not in alfabeto:
            return print(f'símbolo ({symbol}) não pertence ao alfabeto')

        # Verificação se há uma regra de transição para o símbolo e estado atual
        if (estado_atual, symbol) not in transições:
            return print(f'transição ({estado_atual},{symbol}) não existe')

        # Atualização do estado atual
        estado_atual = transições[(estado_atual, symbol)]

    # Verificação se o estado atual é um estado final
    return estado_atual in estado_final

def ler_entrada():
    input_string = input("Informe a palavra: ")
    return input_string

def ler_arquivo(caminho):
    with open(caminho, "r") as file:
        input_string = file.read().replace('\n', '')
    return input_string


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