"""
Trabalho final - Linguagens Formais e Autômatos

grupo:
    - Murilo Sterchile
    - Arthur Sauer
    - Luca Boni

"""
# Esse arquivo contem as seguintes definições:
#   alfabeto ->  lista
#   estados  ->  conjunto
#   estado_inicial -> string
#   estado_final -> conjunto
#   transições  -> dicionário

# símbolos pertencentes ao alfabeto da linguagem
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1']

# estados do automato
estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22'}

# estado inicial
estado_inicial = 'q0'

# estados final
estado_final = {'q0'}

# transiçôes do automato
transições = {
    ('q0', 'l'): 'q1',      #Inicia a máquina
    ('q1', 'o'): 'q1',      #Máquina fica aguardando
    ('q1', 'c'): 'q2',      #Escolhe o tipo de produto: Chocolate
    ('q1', 'b'): 'q3',      #Escolhe o tipo de produto: Batata Chips
    ('q1', 'g'): 'q4',      #Escolhe o tupo de produto: Goma de mascar
    ('q2', 's'): 'q6',      #Escolhe o produto: Chocolate simples
    ('q2', 'p'): 'q7',      #Escolhe o produto: Chocolate uva passa
    ('q2', 'm'): 'q8',      #Escolhe o produto: Chocolate morango
    ('q3', 'f'): 'q9',      #Escolhe o produto: Batata red pepper
    ('q3', 'q'): 'q10',     #Escolhe o produto: Batata queijo
    ('q3', 'h'): 'q11',     #Escolhe o produto: Batata hot dog
    ('q4', 'a'): 'q12',     #Escolhe o produto: Goma amora
    ('q4', 'i'): 'q13',     #Escolhe o produto: Goma iogurte
    ('q4', 'j'): 'q14',     #Escolhe o produto: Goma jabuticaba
    ('q3', 'r'): 'q9',      #Escolhe o produto: Batata red
    ('q6', 'x'): 'q15',     #Confirma o produto
    ('q7', 'x'): 'q15',     #Confirma o produto
    ('q8', 'x'): 'q15',     #Confirma o produto
    ('q9', 'x'): 'q15',     #Confirma o produto
    ('q10', 'x'): 'q15',    #Confirma o produto
    ('q11', 'x'): 'q15',    #Confirma o produto
    ('q12', 'x'): 'q15',    #Confirma o produto
    ('q13', 'x'): 'q15',    #Confirma o produto
    ('q14', 'x'): 'q15',    #Confirma o produto
    ('q15', '1'): 'q15',    #Seleciona a quantidade
    ('q15', 'k'): 'q5',     #Termina a escolha
    ('q15', 'y'): 'q1',     #Cancela
    ('q5', 't'): 'q17',     #Forma de pagamento: Cartão
    ('q5', 'f'): 'q18',     #Forma de pagamento: Dinheiro
    ('q5', 'z'): 'q18',     #Forma de pagamento: Pix
    ('q17', 'u'): 'q21',    #Seleciona o tipo de cartão: Crédito
    ('q17', 'w'): 'q20',    #Seleciona o tipo de cartão: Débito
    ('q18', 'e'): 'q5',     #Troca a forma de pagamento
    ('q19', 'e'): 'q5',     #Troca a forma de pagamento
    ('q20', 'e'): 'q5',     #Troca a forma de pagamento
    ('q21', 'e'): 'q5',     #Troca a forma de pagamento
    ('q22', 'n'): 'q5',     #Pagamento foi recusado
    ('q22', 'v'): 'q1',     #Pagamento foi aceito
    ('q18', 'a'): 'q22',    #Confirmar forma de pagamento
    ('q19', 'a'): 'q22',    #Confirmar forma de pagamento
    ('q20', 'a'): 'q22',    #Confirmar forma de pagamento
    ('q21', 'a'): 'q22',    #Confirmar forma de pagamento
    ('q1', 'd'): 'q0',      #Desliga a máquina
}




