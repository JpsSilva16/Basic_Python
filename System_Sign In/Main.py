import time
import csv

from util import cadastrar, pesquisar, apresentar, menu 

# Suas listas de dados iniciais
nomes = []
tels = []


with open(r"C:\Users\João Pedro\Desktop\Coisa do Jão\Visual Code\Arquivos\nomes_telefones_grande.csv", "r", encoding="utf-8-sig") as arquivo:
    dados = csv.DictReader(arquivo)

    for pessoa in dados:

        nomes.append(pessoa["nome"])
        tels.append(pessoa["telefone"])

while True:

    menu()
    opcao = int(input(f'\nDigite opção desejada: '))

    match opcao:
        
        # Cadastro
        case 1:
            while True:
                c_nome = str(input(f'\nInsira o nome do novo cadastrante: '))
                if c_nome in nomes:
                    time.sleep(0.5)
                    print('Esse nome já está cadastrado')
                    continue
                else:
                    break
            while True:
                c_tel = str(
                    input(f'Insira o telefone do novo cadastrante: '))
                if c_tel in tels:
                    time.sleep(0.5)
                    print('Esse telefone já está cadastrado')
                    continue
                else:
                    print(f'\nFazendo seu cadastro...')
                    break

            cadastrar(c_nome, c_tel)

        # Pesquisa
        case 2:
            search = str(input(f"\nDigite um nome ou número: ")).strip()
            if search:
                print(f'\nPesquisando...\n')
                pesquisar(search)
            else:
                print('Não foi encontrado esse nome ou número.')

        # Apresentar
        case 3:
            type_print = int(input(
                f'\nDigite o numero correspondente ao que desejar imprimir:\n1 - Nomes\n2 - Telefone\n3 - Nomes/Numero\nImprimir: '))
            print(f'Imprimindo...\n')
            apresentar(type_print)

        # Remover
        case 4:
            ...

        # Sair
        case 5:
            print(f'Encerrando sistema...')
            break

        # "Erro"
        case _:
            print('Escolha uma opção válida')
