from funcionario import Funcionario
from produto import Produto
from venda import Venda
class Empresa:
    def __init__(self,listar_func,lsitar_produtos,listar_vendas):
        self.listar_func = listar_func
        self.listar_prods = lsitar_produtos
        self.listar_vendas =listar_vendas
        
    def cadastrar_funcionarios(self,id_fun,nome,cargo,salario):
        funcionario =Funcionario(id_fun,nome,cargo,salario)
        self.listar_func.append(funcionario)
        return f"Funcnionário cadastrado."
        
    def listar_funcionario(self):
        for func in self.listar_func:
            (f"{func.exibir_dados()}")
            break
        
    
    def cadastar_produto(self,id_produto,nome,preco,quantidade):
        produto = Produto(id_produto,nome,preco,quantidade)
        self.listar_prods.append(produto)
        return f'Produto cadastrado'
    
    def lista_produtos(self):
        for prod in self.listar_prods:
            (f"{prod.exibir_produtos()}")
            
    def registrar_vendas(self,id_venda,quantidade_venda,valor_total):
        venda = Venda(id_venda,quantidade_venda,valor_total)

        
        self.listar_vendas.append(venda)
        return "Registro de venda concluido."
        
        
empresa1 = Empresa([],[],[])
# empresa1.cadastar_produto(123,"Dell vale",6.99,1)
# empresa1.lista_produtos()
print(empresa1.registrar_vendas(1,4,0,2,"bbb",5,2))