from src.agendamento.agenda import Agenda

def test_exibir_tarefa_valida():
    agenda = Agenda()
    agenda.adicionar_tarefa("Fazer compras", "2023-09-30")
    tarefa_texto = agenda.exibir_tarefa(0)
    assert tarefa_texto == "Tarefa: Fazer compras deve ser concluída até 2023-09-30"

def test_exibir_tarefa_invalida():
    agenda = Agenda()
    tarefa_texto = agenda.exibir_tarefa(0)
    assert tarefa_texto == "Índice de tarefa inválido."

