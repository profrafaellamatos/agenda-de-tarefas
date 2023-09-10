from src.agendamento.tarefa import Tarefa

def test_criar_tarefa():
    tarefa = Tarefa("Fazer compras", "2023-09-30")
    assert tarefa.titulo == "Fazer compras"
    assert tarefa.data_vencimento == "2023-09-30"