from src.agendamento.tarefa import Tarefa

def test_str_tarefa():
    tarefa = Tarefa("Fazer compras", "2023-09-30")
    assert str(tarefa) == "Tarefa: Fazer compras deve ser concluída até 2023-09-30"