from produto import Produto
class Venda:
    def __init__(self,id_venda,quantidade,valor_total,id_produto,nome,preco):
         self.id_venda = id_venda
         self.produto = Produto(id_produto,nome,preco)
         self.quantidade = quantidade
         self.valor_total = valor_total
    
    def calcular_total(self):
        total = self.quantidade * self.produto.preco
        self.valor_total = total
        return f"Valor total: {self.valor_total}"     
    
    def exibir_Vendas(self):
        print(f"""
[1]| ID: {self.id_venda}
[2]| Quantidade: {self.quantidade}
[3]| Valor Total: {self.valor_total}         
""")
        print(f"[4] Produto: {self.produto.exibir_produtos()}")
        
        
# v1 = Venda(123,2,0,1,"abc",8)
# print(v1.calcular_total())