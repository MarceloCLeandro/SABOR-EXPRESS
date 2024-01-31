import os

restaurantes = [{'nome' : 'Podrão do Zé', 'categoria' : 'Comida de rua', 'ativo' : False},
                {'nome' : 'Churrascaria do Gaúcho', 'categoria' : 'Churrasco', 'ativo' : True}]

def exibir_nome_do_programa():
#site para mudar formatção de letras no terminal https://fsymbols.com/pt/letras/
    print('''
╔═══╗──╔╗───────╔═══╗
║╔═╗║──║║───────║╔══╝
║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
───────────────────────║║
───────────────────────╚╝
      ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o App')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu de opções ')
    main()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja Cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante} cadastrado: ')
    informacoes_do_cadastro = {'nome' : nome_do_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(informacoes_do_cadastro)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes cadastrados')
    print(f'   {'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status\n\n')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_do_restaurante.ljust(25)} | {categoria.ljust(25)} | {ativo}')
    voltar_ao_menu()

def status_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    verificar_restaurante = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            verificar_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi {nome_do_restaurante} desativado com sucesso'
            print(mensagem)

    if not verificar_restaurante:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))# contertendo a String em Inteiro 
        #print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()