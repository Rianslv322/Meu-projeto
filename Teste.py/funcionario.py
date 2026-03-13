class FUncionario:
    def __init__(self,id_fun,nome,cargo,salario):
        self._id_funcionario = id_fun
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def exibir_dados(self):
        print(f"""
| ID: {self.id_funcioanrio}
| Nome: {self.nome}
| Cargo: {self.cargo}
| salário: {self.salario}""")
        
        
    def aumentar_Salario(self,valor):
        self.salario = valor
        return f"Recebimento de Aumento de R${valor} Reais."
    
    