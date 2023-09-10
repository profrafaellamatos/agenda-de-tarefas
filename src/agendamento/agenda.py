from src.agendamento.tarefa import Tarefa

class Agenda:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, data_vencimento):
        tarefa = Tarefa(titulo, data_vencimento)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas
    
    def exibir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            return str(self.tarefas[indice])
        else:
            return "Índice de tarefa inválido."
        
    def __str__(self):
        return "\n".join([str(tarefa) for tarefa in self.tarefas])