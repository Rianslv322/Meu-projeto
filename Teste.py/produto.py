class Produto:
    def __init__(self,id_produto,nome,preco,quantidade_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade_estoque
        
    
    def exibir_produtos(self):
        print(f"""
| ID: {self.id_produto}
| Nome: {self.nome}
| Preço: {self.preco}
|Quantidade: {self.quantida}""")
        
    def adicionar_Estoque(self):
        nome = input("Nome do Produto: ")
        qtdd = int(input("Quantidade: "))
        
        self.quantidade = {nome: f"Quantidade:{qtdd} "}
        print("Produtos adicionados")
        
        for nome_produto, quantidade_produto in self.quantidade.items():
            print(f"""
|{nome_produto}
|{quantidade_produto}
""")
        
        
        
p1 = Produto(12,"banana",1.5,6)
p1.adicionar_Estoque()
