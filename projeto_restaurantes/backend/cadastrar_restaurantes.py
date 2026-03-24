import os
import sys

restaurantes = [{'nome': 'Restaurante A', 'endereco': 'Rua A, 123', 'telefone': '1234-5678'},
                {'nome': 'Restaurante B', 'endereco': 'Rua B, 789', 'telefone': '5555-5555'},
                {'nome': 'Restaurante C', 'endereco': 'Rua C, 456', 'telefone': '9876-5432'}]

def exibir_nome_do_programa():
    print("""
╔════════════════════════════════════╗
║       CADASTRAR RESTAURANTES       ║
╚════════════════════════════════════╝
""")

def exibir_opcaos():
    print("1. Cadastrar novo restaurante")
    print("2. Listar restaurantes cadastrados")
    print("3. Alterar informações de um restaurante")
    print("4. Sair")

def finalizar_app():
    exibir_subtitulo("App finalizado")
    sys.exit()

def voltar_menu():
    input("\nPressione uma tecla para voltar ao menu...")
    main()

def opcao_invalida():
    print("Opção inválida. Por favor, tente novamente.\n")
    voltar_menu()

def exibir_subtitulo(subtitulo):
    os.system('clear')
    linha = '*' * len(subtitulo)
    print(f"{subtitulo}\n{linha}\n")
    print()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastrar novo restaurante")
    nome = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    telefone = input("Digite o telefone do restaurante: ")
    
    restaurante = {'nome': nome, 'endereco': endereco, 'telefone': telefone}
    restaurantes.append(restaurante)
    
    print("\nRestaurante cadastrado com sucesso!")
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo("Restaurantes cadastrados")
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for idx, restaurante in enumerate(restaurantes, start=1):
            print(f"{idx}. {restaurante['nome']} - {restaurante['endereco']} - {restaurante['telefone']}")
    voltar_menu()

def alterar_informacoes():
    exibir_subtitulo("Alterar informações de um restaurante")
    if not restaurantes:
        voltar_menu()
        return
    
    try:
        escolha = int(input("\nDigite o número do restaurante que deseja alterar: "))
        if 1 <= escolha <= len(restaurantes):
            restaurante = restaurantes[escolha - 1]
            print(f"\nRestaurante selecionado: {restaurante['nome']}")
            nome = input("Digite o novo nome (deixe em branco para manter o atual): ")
            endereco = input("Digite o novo endereço (deixe em branco para manter o atual): ")
            telefone = input("Digite o novo telefone (deixe em branco para manter o atual): ")
            
            if nome:
                restaurante['nome'] = nome
            if endereco:
                restaurante['endereco'] = endereco
            if telefone:
                restaurante['telefone'] = telefone
            
            print("\nInformações do restaurante atualizadas com sucesso!")
        else:
            print("Número inválido. Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    
    voltar_menu()

def escolher_opcao():
    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
        cadastrar_restaurante()
    elif opcao == '2':
        listar_restaurantes()
    elif opcao == '3':
        alterar_informacoes()
    elif opcao == '4':
        finalizar_app()
    else:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    while True:
        exibir_opcaos()
        escolher_opcao()

if __name__ == "__main__":
    main()


