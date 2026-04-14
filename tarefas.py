tarefas = []

def adicionar_tarefa(nome):
    tarefas.append({"nome": nome, "concluida": False})

def listar_tarefas():
    return tarefas

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)