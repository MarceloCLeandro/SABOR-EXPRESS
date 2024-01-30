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
    os.system('cls')
    print('Finalizando o App\n')

def opcao_invalida():
    print('Opção Invalida!\n')
    input('Digite uma tecla para voltar ao menu de opções ')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do Restaurante que deseja Cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    input('Digite uma tecla para voltar ao menu de opções ')
    main()

def listar_lestaurantes():
    pass

def ativar_restaurante():
    pass

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))# contertendo a String em Inteiro 
        #print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_lestaurantes()
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