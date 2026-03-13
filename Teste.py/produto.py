class Produto:
    def __init__(self,id_produto,nome,preco,quantidade):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def exibir_produtos(self):
        print(f"""
DADOS PRODUTO
[1]| ID: {self.id_produto}
[2]| Nome: {self.nome}
[3]| Preço: {self.preco}
[4]|Quantidade: {self.quantidade}""")
        
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
                
