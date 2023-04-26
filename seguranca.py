import pyrebase

config = {
    "apiKey": "AIzaSyD2jmjs3YC0DmpIe84lAkSUn5Y4XZyprns",
    "authDomain": "sistemas-da-informa.firebaseapp.com",
    "projectId": "sistemas-da-informa",
    "storageBucket": "sistemas-da-informa.appspot.com",
    "messagingSenderId": "498268291282",
    "appId": "1:498268291282:web:5e7fbc0ae7869bc9b6ad0b",
    "measurementId": "G-YS315ZEEXG",
    "databaseURL": "",
}

# autentica aplicação
firebase = pyrebase.initialize_app(config)

# Autenticação do app
auth = firebase.auth()
# Criação de conta de usuário

def autenticar():
    # Autenticação do usuário
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")
    try:
        usuario = auth.sign_in_with_email_and_password(email,senha)
        print("Usuário autenticado com sucesso")
        dados_usuario = auth.get_account_info(usuario['idToken'])
        print(dados_usuario)
        main_secundadrio(email)

    except:
            print("Erro de login,por favor tente novamente")
            autenticar()



# Autenticação do usuário
def criar_usuario():
    # Criação de conta de usuário
    email = input("Digite o e-mail do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    try:
        usuario = auth.create_user_with_email_and_password(email,senha)
        print("Usuário criado com sucesso")
        auth.send_email_verification(usuario['idToken'])
        print("Por favor ,confirme o seu email cadastrado ,acessando o seu email e confirmando o link enviado para o seu email.")
        dados_usuario = auth.get_account_info(usuario['idToken'])
        print(dados_usuario)


    except:
        print("Erro de cadastro,tente novamente.")
        criar_usuario()



def resetar_senha():
    email = input("Digite o e-mail do usuário para recuperar a senha: ")
    try:
        auth.send_password_reset_email(email)
        print("E-mail de recuperação de senha enviado com sucesso")
    except:
        print("Erro,esse email não está cadastrado")
        resetar_senha()


def main_secundadrio(mail):
    print("1-Ler um arquivo")
    print("2-Escrever no arquivo")
    print("4-Deletar o arquivo")
    option = int(input("Digite um valor:"))
    if (option == 1):
        ler_arquivo(mail)
    elif (option == 2):
        escrever_arquivo(mail)

def ler_arquivo(email):
    with open('arquivo.txt', 'r') as arquivo:
        i = 0
        while (i < 1):
            permissoes = arquivo.readlines(i)
            for linha in permissoes:
                linha = linha.replace("\n","")
                campo = linha.split(",")
                usuarios = campo[0]
                arquivo = campo[1]
                permition = campo[2]
                permition2=campo[3]
                permition3=campo[4]
            arquivos = input("Digite o nome do arquivo em que voce deseja realizar uma operação:")

            if email == usuarios and arquivo==arquivos and ( permition == "leitura" or permition2=="leitura" or permition3=="leitura"):
                print("Acesso permitido")
                with open(arquivos,'r') as leitura:
                    print("o arquivo {} foi lido".format(arquivos))
                    x = leitura.readlines()
                    print(x)
            else:
                print("Acesso negado")
            print("1-Voltar ao menu principal")
            print("2-Ler um outro arquivo")
            print("3-Encerrar o programa")
            option2 = int(input("Selecione a opcao desejada:"))
            if(option2==1):
                main_secundadrio(email)
            elif (option2 == 2):
                ler_arquivo(email)
            elif(option2==3):
                exit()


def escrever_arquivo(email):
    with open('arquivo.txt', 'r') as arquivo:
        i = 0
        while (i < 1):
            permissoes = arquivo.readlines(i)
            for linha in permissoes:
                linha = linha.replace("\n", "")
                campo = linha.split(",")
                usuarios = campo[0]
                arquivo = campo[1]
                permition = campo[2]
                permition2 = campo[3]
                permition3 = campo[4]
            arquivos = input("Digite o nome do arquivo em que voce deseja realizar uma operação:")
            if email == usuarios and arquivo==arquivos and(permition == "escrever" or permition2=="escrever" or permition3=="escrever"):
                print("Acesso Permitido")
                conteudo=input("Digite um conteudo para ser inserido dentro deste arquivo:")

                with open(arquivos,'w') as escrita:
                    escrita.write(conteudo)
                    print("o arquivo {} foi sobrescrito".format(arquivos))

            else:
                print("Acesso negado")
            print("1-Voltar ao menu principal")
            print("2-Ler um outro arquivo")
            print("3-Encerrar o programa")
            option2 = int(input("Selecione a opção desejada:"))
            if(option2==1):
                main_secundadrio(email)
            elif (option2 == 2):
                ler_arquivo(email)
            elif (option2 == 3):
                exit()

def main():

    print("1-Fazer login")
    print("2-Cadastra-se")
    print("3-Esqueceu senha")
    opcao=int(input("Digite uma opção:"))
    while opcao ==1:
        autenticar()
        break
    while opcao ==2:
        criar_usuario()
        break
    while opcao == 3:
        resetar_senha()
        break
    if(opcao>3 or opcao<1):
        print("Opção inválida ,digite novamente")
        main()
main()
