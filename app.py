import os

restaurantes = []

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
    print('3. Ativar Restaurante')
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
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja Cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes cadastrados')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu()

def ativar_restaurante():

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
            ativar_restaurante()
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