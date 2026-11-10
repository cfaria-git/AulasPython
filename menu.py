import runpy

def exibir_menu():
    print("## MENU ##")
    print("1 - Migrar Informações")
    print("2 - Alterar Informações")
    print("3 - Mover planilhas")
    print("4 - Transferir informações entre planilhas")
    print("5 - Sair")

def deseja_continuar():
    while True:
        alt = input("Deseja realizar nova operacao ? (S/N): ").strip().upper()
        if alt == "S":
            print("vc escolheu sim")
            return True
        elif alt == "N":
            print("vc escolheu não")
            return False
        else:
            print("Opção inválida. Verifique!")


while True:
    exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Escolheu a opcao Adição")
        runpy.run_path("calculosnumerico.py")
        deseja_continuar()
    elif opcao == 2:
        print("Rodando o meu script secundario")
        runpy.run_path("comparacao.py")
        deseja_continuar()
    elif opcao == 3:
        print("Escolheu a opcao Multiplicação")
        runpy.run_path("helloword.py")
        deseja_continuar()
    elif opcao == 4:
        print("Escolheu a opcao Divisão")
        runpy.run_path("laco_repeticao.py")
        deseja_continuar()
    elif opcao == 5:
        print("vc escolheu a opcao Sair")
        break
    else:
        print("Opçoes errada")