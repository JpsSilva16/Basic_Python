import time

def cadastrar(nome, telefone):
    global nomes, tels

    nomes.append(nome)
    tels.append(telefone)

    print(f'Cadastro Realizado\n')


def pesquisar(fsearch):
    global nomes, tels
    nomESaux = []
    teLSaux = []

    # Padroniza a busca para minúsculas
    termo = fsearch.lower()

    for i in range(len(nomes)):
        # Verifica se o termo pesquisado está contido no nome OU no telefone
        if termo in nomes[i].lower() or termo in tels[i]:
            nomESaux.append(nomes[i])
            teLSaux.append(tels[i])

    # Exibe os resultados encontrados
    if len(nomESaux) > 0:
        print(f"--- Encontrado(s) {len(nomESaux)} registro(s) ---")
        for i in range(len(nomESaux)):
            print(f'Conta: {nomESaux[i]} | Telefone: {teLSaux[i]}')
            time.sleep(0.5)
    else:
        time.sleep(0.1)
        print('Nenhuma conta foi encontrada com esse termo.')


def apresentar(type):
    global nomes, tels

    for i in range(0, len(nomes)):
        # nomes
        if type == 1:
            print(f'{[i+1]}-{nomes[i]}')
            time.sleep(0.1)
        # telefone
        elif type == 2:
            print(f'{[i+1]}-{tels[i]}')
            time.sleep(0.1)
        # ambos
        else:
            print(f'{[i+1]}- Conta: {nomes[i]} | Telefone: {tels[i]}')
            time.sleep(0.1)


def menu():
    print('''\n
    |======MENU======|
    [1] - Cadastrar
    [2] - Pesquisa
    [3] - Apresentar
    [4] - Remover
    [5] - Sair
    |======++++======|''')