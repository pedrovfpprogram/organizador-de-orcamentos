import sqlite3
conexao = sqlite3.connect('orcamentos.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orcamentos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    contato TEXT NOT NULL,
    servico TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL)''')
def salvar_dados():
    cursor.execute('SELECT * FROM orcamentos ORDER BY id ASC')
    orcamentos = cursor.fetchall()
    dados = []
    if not orcamentos:
        return False
    for orcamento in orcamentos:
        dados.append(orcamento)
    conexao.commit()
    return dados
def add():
    nome_cliente = input("Digite o nome do cliente: ")
    contato_cliente = input("Digite o contato do cliente: ")
    servico_realizado = input("Digite o serviço que foi realizado: ")
    valor_cobrado = float(input('Digite o valor que foi cobrado: '))
    data_realizacao = input("Digite a data do serviço: ")
    cursor.execute('INSERT INTO orcamentos (cliente,contato,servico,valor,data) VALUES (?,?,?,?,?)',(nome_cliente,contato_cliente,servico_realizado,valor_cobrado,data_realizacao))
    conexao.commit()
    print("Usuário adicionado com sucesso ✅")
def init():
    while True:
        print(f'''{'-'*50}Gerenciador do banco de dados{'-'*50}

📋 Menu
    1️⃣  Adicionar servicos
    2️⃣  Editar serivcos
    3️⃣  Remover servicos
    4️⃣  Visualizar serviços''')
        try:
            opcao = int(input('Digite uma das opções anteriores: '))
        except ValueError:
            print('Digite apenas números')
            break
        match opcao:
            case 1:
                add()
        break