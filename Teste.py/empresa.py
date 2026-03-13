from funcionario import Funcionario
from produto import Produto
from venda import Venda
class Empresa:
    def __init__(self,listar_func,lsitar_produtos,listar_vendas):
        self.listar_func = listar_func
        self.listar_prods = lsitar_produtos
        self.listar_vendas =listar_vendas
        
    def cadastrar_funcionarios(self):
        id_fun = int(input("Id Funcionário -> "))
        nome = str(input("Nome Funcionário: -> "))
        cargo = str(input("Cargo Funcionário -> "))
        salario = float(input("salário Funcionário -> "))
        funcionario =Funcionario(id_fun,nome,cargo,salario)
        self.listar_func.append(funcionario)
        print(f"Funcnionário cadastrado.")
        
    def listar_funcionario(self):
        for func in self.listar_func:
            (f"{func.exibir_dados()}")
    
    def cadastar_produto(self):
        id_produto = int(input("Id Produto -> "))
        nome = str(input("Nome Produto -> "))
        preco = float(input("Preço Produto -> "))
        quantidade = int(input("Quantidade Produto -> "))
        produto = Produto(id_produto,nome,preco,quantidade)
        self.listar_prods.append(produto)
        print(f'Produto cadastrado')
    
    def lista_produtos(self):
        for prod in self.listar_prods:
            (f"{prod.exibir_produtos()}")
            
    def registrar_vendas(self):
        id_venda = int(input("Id venda -> "))
        quantidade_venda = int(input("Quantidade venda -> "))
        valor_total = float(input("Valor Total venda -> "))
        id_produto = int(input("Id Produto -> "))
        nome = str(input("Nome produto -> "))
        preco = float(input("Preço produto -> "))
        quantidade = int(input("Quantidade Produto -> "))
        venda = Venda(id_venda,quantidade_venda,valor_total,id_produto,nome,preco,quantidade)
        self.listar_vendas.append(venda)
        return ("Registro de venda concluido.")
    
    def lista_venda(self):
        for x in self.listar_vendas:
            (f"{x.exibir_Vendas()}")
        
