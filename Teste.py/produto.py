class Produto:
    def __init__(self,id_produto,nome,preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade ={}
        
    
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
            
    def remover_Estoques(self):
        nome = input("Nome do Produto: ")
        if nome in self.quantidade:
            self.quantidade.pop(nome)
            print("Removido.")
        else:
            print("Chave não encontrada.")
                
p1 = Produto(123, "banana", 1.90)
p1.adicionar_Estoque()
p1.remover_Estoques()