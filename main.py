# main.py
import estoque

# Carregar os dados ao iniciar o programa
estoque.carregar_dados()
estoque.carregar_movimentacoes()
# Loop principal do programa
while True:
    print("\nMenu de Opcoes:")
    print("1 - Cadastrar Produto")
    print("2 - Pesquisar Produto")
    print("3 - Historico de Movimentacoes")
    print("4 - Editar Produto")
    print("5 - Sair")
    
    interacao = input("Escolha uma opcao: ")

    if interacao == "1":
        nome = input("Digite o nome: ")
        categoria = input("Digite a categoria: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
        localizacao = input("Digite a localização: ")
        estoque.cadastro(nome, categoria, quantidade, preco, localizacao)   
    
    elif interacao == "2":
        estoque.pesquisar_produto_por_nome()
    
    elif interacao == "3":
        print("Abrindo Movimentacoes...")
        estoque.historico_movimentacao_produto()
    
    elif interacao == "4":
        estoque.editar_produto()
    
    elif interacao == "5":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
