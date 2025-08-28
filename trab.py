
def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cursos disponíveis")
    print("2 - Cursos feitos")
    print("3 - Certificados")
    print("4 - Sair")

def listar_cursos_disponiveis(cursos):
    print("\nCursos disponíveis:")
    if cursos:
        for i, (nome, link) in enumerate(cursos.items(), 1):
            print(f"{i}. {nome}")
        
        escolha = input("\nDigite o número do curso para ver o link (ou Enter para voltar): ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(cursos):
                nome = list(cursos.keys())[escolha - 1]
                print(f"\nLink do curso {nome}: {cursos[nome]}")
            else:
                print("Número inválido.")
        else:
            print("Voltando ao menu...")
    else:
        print("Nenhum curso disponível no momento.")

def listar_cursos_feitos(cursos):
    print("\nCursos feitos:")
    if cursos:
        for i, c in enumerate(cursos, 1):
            print(f"{i}. {c}")
    else:
        print("Você ainda não concluiu nenhum curso.")

def listar_certificados(cursos_feitos, certificados):
    print("\nCertificados:")
    exibiu = False
    for curso in cursos_feitos:
        if curso in certificados:
            print(f"- {certificados[curso]}")
            exibiu = True
    if not exibiu:
        print("Nenhum certificado disponível.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            listar_cursos_disponiveis(CURSOS_DISPONIVEIS)

        elif opcao == "2":
            listar_cursos_feitos(CURSOS_FEITOS)

        elif opcao == "3":
            listar_certificados(CURSOS_FEITOS, CERTIFICADOS)

        elif opcao == "4":
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    CURSOS_DISPONIVEIS = {
        "Word Básico": "https://exemplo.com/word-basico",
        "Inglês Básico": "https://exemplo.com/ingles-basico",
        "Excel Básico": "https://exemplo.com/excel-basico"
    }

    CURSOS_FEITOS = [
        "Word Básico"
    ]

    CERTIFICADOS = {
        "Word Básico": "Certificado de Conclusão - Word Básico"
    }

    main()
