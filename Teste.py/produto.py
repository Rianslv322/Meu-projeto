class Produto:
    def __init__(self,id_produto,nome,preco,quantidade_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade_estoque
        
    
    def exibir_produtos(self)