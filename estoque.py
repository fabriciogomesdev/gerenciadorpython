# estoque.py
import uuid
import datetime

tempo = datetime.datetime.now()
formato_tempo = tempo.strftime("%d/%m/%Y %H:%M:%S")

# Variáveis globais para armazenar dados
produtos = []
movimentacoes = []

# Função para carregar os dados do arquivo 'dados.txt'
def carregar_dados():
    try:
        with open('dados.txt', 'r') as arquivo:
            for linha in arquivo.readlines():
                dados = linha.strip().split(';')
                if len(dados) < 7:
                    print(f"Linha inválida: {linha}")
                    continue
                produto = {
                    'id_produto': dados[0],
                    'nome': dados[1],
                    'categoria': dados[2],
                    'quantidade': int(dados[3]),
                    'preco': float(dados[4]),
                    'localizacao': dados[5],
                    'tempo': dados[6],
                }
                produtos.append(produto)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Criando um novo.")


def carregar_movimentacoes():
    try:
        with open('movimentacao.txt', 'r') as arquivo:
            for linha in arquivo.readlines():
                dados = linha.strip().split(';')
                if len(dados) < 7:
                    print(f"Linha inválida: {linha}")
                    continue
                produto = {
                    'id_produto': dados[0],
                    'nome': dados[1],
                    'categoria': dados[2],
                    'quantidade': int(dados[3]),
                    'preco': float(dados[4]),
                    'localizacao': dados[5],
                    'tempo': dados[6],
                }
                movimentacoes.append(produto)
    except FileNotFoundError:
        print("Arquivo de movimentações não encontrado. Criando um novo.")


# Função para salvar os dados no arquivo 'dados.txt'
def salvar_dados():
    with open('dados.txt', 'w') as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto['id_produto']};{produto['nome']};{produto['categoria']};{produto['quantidade']};{produto['preco']};{produto['localizacao']};{produto['tempo']}\n")

def salvar_movimentacoes():
    with open('movimentacao.txt', 'w') as arquivo:
        for produto in movimentacoes:
            arquivo.write(f"{produto['id_produto']};{produto['nome']};{produto['categoria']};{produto['quantidade']};{produto['preco']};{produto['localizacao']};{produto['tempo']}\n")
# Função para cadastrar um novo produto

def cadastro(nome, categoria, quantidade, preco, localizacao):
    id_produto = str(uuid.uuid4())
    
    novoproduto = {
        'id_produto': id_produto,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        'localizacao': localizacao,
        'tempo': formato_tempo 
    }
    produtos.append(novoproduto)
    movimentacoes.append(novoproduto)
    salvar_dados()
    salvar_movimentacoes()
    print("Produto cadastrado com sucesso!")
   
# Função para editar um produto existente
def editar_produto():

    nome_produto = input("Digite o nome do produto que deseja editar: ")
    produtos
    for i, produto in enumerate(produtos):
        if produto['nome'] == nome_produto:
            print("Produto encontrado!")
            novo_nome = input(f"Nome ({produto['nome']}): ") or produto['nome']
            nova_categoria = input(f"Categoria ({produto['categoria']}): ") or produto['categoria']
            nova_quantidade = input(f"Quantidade ({produto['quantidade']}): ") or produto['quantidade']
            novo_preco = input(f"Preço ({produto['preco']}): ") or produto['preco']
            nova_localizacao = input(f"Localização ({produto['localizacao']}): ") or produto['localizacao']
            declararid = produto['id_produto']
            produtos[i] = {
                'id_produto': produto['id_produto'],
                'nome': novo_nome,
                'categoria': nova_categoria,
                'quantidade': int(nova_quantidade),
                'preco': float(novo_preco),
                'localizacao': nova_localizacao,
                'tempo': produto['tempo'],
            }
            
            salvar_dados()
            edit_movimentacao(declararid, novo_nome, nova_categoria, nova_quantidade, novo_preco, nova_localizacao, )
            print("Produto editado com sucesso!")
            return
    print("Produto não encontrado.")

def edit_movimentacao(declararid, novo_nome, nova_categoria, nova_quantidade, novo_preco, nova_localizacao, ):
    novoproduto = {
        'id_produto': declararid,
        'nome': novo_nome,
        'categoria': nova_categoria,
        'quantidade': nova_quantidade,
        'preco': novo_preco,
        'localizacao': nova_localizacao,
        'tempo': formato_tempo 
    }
    movimentacoes.append(novoproduto)
    salvar_movimentacoes()

# Função para pesquisar produto por nome
def pesquisar_produto_por_nome():
    nome = input("Digite o nome do produto: ").lower()
    for produto in produtos:
        if produto['nome'].lower() == nome:
            print(f"Produto encontrado: ID={produto['id_produto']}, Nome={produto['nome']}, Categoria={produto['categoria']}, Quantidade={produto['quantidade']}, Preço={produto['preco']}, Localização={produto['localizacao']}")
            return
    print("Produto não encontrado.")

# Função para exibir histórico de movimentações


def historico_movimentacao_produto():
    produto_desejado = input("Digite o nome do produto: ").lower()
    for produto in movimentacoes:
        if produto['nome'].lower() == produto_desejado:
            print(produto)
