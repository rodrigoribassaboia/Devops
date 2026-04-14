from tarefas import *

def menu():
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Atualização para PR")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            adicionar_tarefa(nome)

        elif opcao == "2":
            lista = listar_tarefas()
            for i, t in enumerate(lista):
                status = "✔" if t["concluida"] else "✘"
                print(f"{i} - {t['nome']} [{status}]")

        elif opcao == "3":
            indice = int(input("Índice da tarefa: "))
            concluir_tarefa(indice)

        elif opcao == "4":
            indice = int(input("Índice da tarefa: "))
            remover_tarefa(indice)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

print("CI/CD funcionando!")

if __name__ == "__main__":
    menu()