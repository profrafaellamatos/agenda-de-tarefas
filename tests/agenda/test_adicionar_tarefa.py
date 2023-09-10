from src.agendamento.agenda import Agenda

def test_adicionar_tarefa():
    agenda = Agenda()
    agenda.adicionar_tarefa("Fazer compras", "2023-09-30")
    assert len(agenda.listar_tarefas()) == 1