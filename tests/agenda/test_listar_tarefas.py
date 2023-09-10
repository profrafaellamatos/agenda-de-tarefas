from src.agendamento.agenda import Agenda

def test_listar_tarefas():
    agenda = Agenda()
    agenda.adicionar_tarefa("Fazer compras", "2023-09-30")
    agenda.adicionar_tarefa("Estudar Python", "2023-10-15")
    tarefas = agenda.listar_tarefas()
    assert len(tarefas) == 2
    assert "Fazer compras" in str(agenda)
    assert "Estudar Python" in str(agenda)