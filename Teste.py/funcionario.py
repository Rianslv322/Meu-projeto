class Funcionario:
    def __init__(self,id_fun,nome,cargo,salario):
        self.id_funcionario = id_fun
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def exibir_dados(self):
        print(f"""
DADOS DO FUNCIONÀRIO
[1]| ID: {self.id_funcionario}
[2]| Nome: {self.nome}
[3]| Cargo: {self.cargo}
[4]| salário: {self.salario}""")
        
    def aumentar_Salario(self,valor):
        self.salario = valor
        return f"Recebimento de Aumento de R${valor} Reais."
    
