from gramatica import alfabeto, estado_inicial, estado_final, transições

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

while True:

    k = input("\ninforme a palavra: ")

    j = automato(k)

    if j == True:
        print("palavra aceita")
    else:
        print("palavra rejeitada")

    k = input('deseja realizar mais uma operação: (s) sim ou (n) não \n')

    if k == "n":
        break