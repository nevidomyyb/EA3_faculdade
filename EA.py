import os

# Lista de usuários contendo cada usuário como um dicionário.
usuarios = [
    {'user': 'Pedro', 'password': '123456', 'name': 'Pedro Cunha'}
]


def criar_usuario(user, password, name):
    # Função para criar usuário
    usuarios.append({'user': user, 'password': password, 'name': name})
    print(f'Usuário [{name}] criado com sucesso.')


def get_usuario_e_validar():
    # Função de validar se um usuário já existe
    while True:
        userInputCadastro = str(input('Usuário: '))
        for usuario in usuarios:
            if userInputCadastro == usuario['user']:
                print('Este usuário já existe')
                continue
            else:
                return userInputCadastro


def autenticar(user, password):
    # Função para autenticar o usuário no sistema
    # Retorna o name do usuário caso seja autenticado, ou False quando não encontra um usuário/senha compatíveis
    # Esse retorno é usado em outras funções como a de excluir e também no próprio sistema.
    for usuario in usuarios:
        if (user == usuario['user'] and password == usuario['password']):
            is_authenticated = usuario['name']
            break
        else:
            is_authenticated = False
    return is_authenticated


def excluir_usuario(user, adminpassword, user_logado_name):
    # Função para excluir usuário com base no user
    # Possui uma validação se o usuário que está tentando excluir é o usuário logado
    for usuario in usuarios:
        if usuario['name'] == user_logado_name:
            user_logado = usuario['user']
    if (user == user_logado):
        print(f'Você não pode excluir o usuário atual')
        return

    indice = 0
    for usuario in usuarios:
        if (user == usuario['user'] and adminpassword == '070663'):
            print(f'Usuário {user} excluido com sucesso')
            del (usuarios[indice])
            return
        indice += 1
        print(f'Usuário não encontrado ou senha administrativa incorreta')


def mostrar_menu():
    # Função para mostrar o menu inicial
    print('[1] Entrar no sistema')
    print('[2] Cadastrar')
    print('[3] Sair')


def mostrar_menu_logado():
    # Função para mostrar o menu quando logar
    print('[1] Excluir usuário')
    print('[2] Listar usuários')
    print('[3] Logout')


def listar_usuarios():
    # Função para listar os usuários
    for usuario in usuarios:
        print('-'*16)
        for key, value in usuario.items():
            if key != 'password':
                print(f'{key} : {value}')


def sistema_logado(is_authenticated):
    # Função do sistema complementar quando o usuário logar
    autenticado = is_authenticated
    while autenticado:
        mostrar_menu_logado()
        opt = int(input('Insira a opção escolhida: '))
        match opt:
            case 1:
                # Usando a função de excluir um usuário
                os.system('cls')
                userInput = str(input('Usuário para excluir: '))
                adminpasswordInput = str(input('Senha administrativa: '))
                excluir_usuario(userInput, adminpasswordInput, autenticado)
            case 2:
                # Usando a função para listar os usuários
                os.system('cls')
                listar_usuarios()
            case 3:
                # Deslogando
                os.system('cls')
                print('Realizando Logout')
                autenticado = None
                return autenticado


while True:
    # Menu inicial do sistema
    mostrar_menu()
    opt = int(input('Insira a opção escolhida: '))
    match opt:
        case 1:
            # Autentica o usuário com base no user e password
            os.system('cls')
            userInput = str(input('Usuário: '))
            passInput = str(input('Senha: '))
            autenticado = autenticar(userInput, passInput)
            if autenticado:
                print(f'{autenticado}, bem-vindo ao sistema')
                autenticado = sistema_logado(autenticado)
            if autenticado == False:
                print('Combinação de usuário e senha incorretos.')
            pass
        case 2:
            # Utilizando a função de cadastrar um novo usuário
            os.system('cls')
            userInputCadastro = get_usuario_e_validar()
            passInputCadastro = str(input('Senha: '))
            nameInputCadastro = str(input('Nome: '))
            criar_usuario(userInputCadastro,
                          passInputCadastro,
                          nameInputCadastro
                          )
            pass
        case 3:
            # Saí do sistema
            os.system('cls')
            print('Saindo...')
            break
