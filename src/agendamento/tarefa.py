class Tarefa:
    def __init__(self, titulo, data_vencimento):
        self.titulo = titulo
        self.data_vencimento = data_vencimento

    #representação de string personalizada
    def __str__(self):
        return f"Tarefa: {self.titulo} deve ser concluída até {self.data_vencimento}"