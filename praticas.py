#Exercícios

#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.\n')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print(f'Meu nome é {nome} e tenho {idade} anos')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir: 
#A
#L
#U
#R
#A

print('''
A
L
U
R
A
''')
#outra maneira é usando o sep="\n" assim vc separa cada item pela virgula como no exemplo a seguir
print('A','L','U','R','A', sep='\n')

#4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e 
#arredondado para apenas duas casas decimais. Para facilitar, utilize:

#pi = 3.14159
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')

#Exercícios 2

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Descubra se um número é PAR ou ÍMPAR, digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#    Criança: 0 a 12 anos;
#    Adolescente: 13 a 18 anos;
#    Adulto: acima de 18 anos.
identificar_idade = int(input('Digite a sua idade: '))
if identificar_idade <= 12:
    print(f'Sua idade é {identificar_idade} e sua classificação é: Criança')
elif identificar_idade > 12 and identificar_idade <= 18:
    print(f'Sua idade é {identificar_idade} e sua classificação é: Adolescente')
else:
    print(f'Sua idade é {identificar_idade} e sua classificação é: Adulto')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
usuario = 'admin'
senha = 'admin'

verificar_usuario = input('Digite o nome de usuário: ')
verificar_senha = input('Digite a senha: ')

if usuario == verificar_usuario and senha == verificar_senha:
    print('Login bem sucedido!')
else:
    print('Credenciais inválidas. Tente novamente.')

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#    Caso contrário: o ponto está localizado no eixo ou origem.

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0:
    print('O ponto está no primeiro quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no terceiro quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no quarto quadrante.')
else:
    print('O ponto está sobre um eixo ou na origem.')
