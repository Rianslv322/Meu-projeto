from produto import Produto
class Venda:
    def __init__(self,id_venda,quantidade_vendas,valor_total,id_produto,nome,preco,quantidade):
         self.id_venda = id_venda
         self.produto = Produto(id_produto,nome,preco,quantidade)
         self.quantidade = quantidade_vendas
         self.valor_total = valor_total
       
    def calcular_total(self):
        total = self.quantidade * self.produto.preco
        self.valor_total = total
        return f"Valor total: {self.valor_total}"     
    
    def exibir_Vendas(self):
        print(f"""
DADOS VENDAS
[1]| ID: {self.id_venda}
[2]| Quantidade: {self.quantidade}
[3]| Valor Total: {self.valor_total}      
""")
        return f"{self.produto.exibir_produtos()}"
