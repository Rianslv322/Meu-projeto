from funcionario import Funcionario
from produto import Produto
from venda import Venda
class Empresa:
    def __init__(self,listar_func,lsitar_produtos,listar_vendas):
        self.listar_func = listar_func
        self.lsitar_produtos = lsitar_produtos
        self.listar_vendas =listar_vendas
        
    def cadastrar_funcionarios(self,id_fun,nome,cargo,salario):
        funcionario =Funcionario(id_fun,nome,cargo,salario)
        self.listar_func.append(funcionario)
        return f"Funcnionário cadastrado."
        
    def listar_funcionario(self):
        for x in self.listar_func:
            print(f"{}")
        
        
em1 = Empresa([],[],[])
print(em1.cadastrar_funcionarios("123","Rian silva","gerente",3000))
print(em1.listar_funcionario())