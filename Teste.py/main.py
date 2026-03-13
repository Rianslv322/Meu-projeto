from empresa import Empresa 

import time
Gerenciamento_de_Produtos = Empresa([],[],[])
while True:
    print("\n╔══════════════════════════════╗")
    print("║      SISTEMA DA EMPRESA      ║")
    print("╠══════════════════════════════╣")
    print("║ 1 ➜ Cadastrar Funcionário    ║")
    print("║ 2 ➜ Listar Funcionários      ║")
    print("║ 3 ➜ Cadastrar Produto        ║")
    print("║ 4 ➜ Listar Produtos          ║")
    print("║ 5 ➜ Registrar Venda          ║")
    print("║ 6 ➜ Listar Vendas            ║")
    print("║ 0 ➜ Sair                     ║")
    print("╚══════════════════════════════╝")

    opcao = int(input("Digite a opção desejada: "))
  
    if opcao == 1:
        
        Gerenciamento_de_Produtos.cadastrar_funcionarios()
    
    if opcao == 2:
        Gerenciamento_de_Produtos.listar_funcionario()
        
    if opcao == 3:
        Gerenciamento_de_Produtos.cadastar_produto()
        
    if opcao == 4:
        Gerenciamento_de_Produtos.lista_produtos()
        
    if opcao == 5:
        Gerenciamento_de_Produtos.registrar_vendas()
        
    if opcao == 6:
        Gerenciamento_de_Produtos.lista_venda()
        
    if opcao == 0 :
        print("Desligando em...")
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        print("Sistema desligado!")
        
        break
            