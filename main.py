import os;

path_atual = os.getcwd()
path_receptaculo = os.path.join(path_atual, "receptaculo.txt")

print(path_receptaculo)

with open(path_receptaculo) as file:
    content = file.read()
    quant_linhas = content.count('\n') + 1

    first_space = content.find('\n')
    resto = content[first_space:].strip()

    line_colunas = resto[resto.find('|'):resto.find('\n')]
    colunas = ', '.join(line_colunas.replace('|', ' ').split())

    quant_colunas = len(colunas.split())

    conteudo_tabela = resto[resto.find('\n'):]
    quant_barras = conteudo_tabela.count('|')

    quant_registros = int(quant_barras / (quant_colunas + 1))

    novo_resto = conteudo_tabela
    quant_linhas_restantes = (novo_resto.strip()).count('\n') + 1

    num_column = 0
    num_row = 0

    cont = 0
    stop = 0
    array_rows = []
    array = []

    while stop == 0:
        novo_resto = novo_resto.strip()
        pos_final = novo_resto.find('\n')
        
        line = novo_resto[0:pos_final]

        isContentLine = True if line.count('|') > 0 else False

        if isContentLine == True:
            array = []

            for e in line.split('|'):
                if e != '':
                    array.append(e.strip())
            
            array_rows.append(array)

        novo_resto = novo_resto[pos_final:]

        cont += 1

        if cont == quant_linhas_restantes:
            stop = 1

    comando = 'INSERT INTO nome_tabela '
    comando += f"({colunas}) "
    comando += f"VALUES "

    for row in array_rows:
        comando += '('
        
        cont = 0
        for col in row:
            elemento = ''

            if cont != 0:
                elemento = ', '

            try:
                float(col)  # Tenta converter para float
                isNumber = True
            except ValueError:
                isNumber = False
        
            if isNumber == True:
                elemento += col
            else:
                elemento += f"'{col}'"

            comando += elemento

            cont += 1
 
        comando += '),'

    comando = comando[0: len(comando) - 1]
    comando += ';'

    print(comando)


    # print(f"O arquivo tem essa quantidade de linhas: {quant_linhas}")
    # print(f"O primeiro \\n esta na posicao: {first_space}")
    # print(f"O resto e: \n{resto}")
    # print(f"Tem {quant_colunas} coluna(s) e ela(s) é(são): {colunas}")
    # print(f"Olha aqui: {conteudo_tabela}")
    # print(f"Quantidade de registros: {quant_registros}")

'''
text = "Olá, mundo! Bem-vindo ao mundo da programação."
substring = "mundo"

# Usando find()
index = text.find(substring)

if index != -1:
    print(f"A substring '{substring}' foi encontrada na posição {index}.")
else:
    print(f"A substring '{substring}' não foi encontrada.")
'''

# with open(path_receptaculo, 'r') as file:
#    content = file.read()
#    print(content)