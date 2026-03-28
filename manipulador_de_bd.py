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
def edit():
    nome = input('Digite o nome do cliente: ')
    try:
        cursor.execute('SELECT * FROM orcamentos WHERE cliente = ? ORDER BY cliente ASC',[nome])
    except:
        print('Usuário não encontrado!')
        return False
    dados = cursor.fetchall()
    print('Exibindo valores encontrados:')
    for item in dados:
        id,cliente,contato,servico,valor,data = item
        print(f'''Id:{id}
Cliente: {cliente}
Contato: {contato}
Serviço: {servico}
Valor: {valor}
Data: {data}
{'='*50}''')
    usuario = input('Digite o id do usuário pra ser editado: ')
    op = input('''Escolha o que editar:
    1️⃣  Nome
    2️⃣  Contato
    3️⃣  Serviço
    4️⃣  Valor
    5️⃣  Data
    ''')
    n_valor = input('Digite o novo valor: ')
    match op:
        case '1':
            cursor.execute('UPDATE orcamentos SET cliente = ? WHERE id = ?', (n_valor,usuario))
            conexao.commit()
            print('Editado com sucesso ✅')
        case '2':
            cursor.execute('UPDATE orcamentos SET contato = ? WHERE id = ?', (n_valor,usuario))
            conexao.commit()
            print('Editado com sucesso ✅')
        case '3':
            cursor.execute('UPDATE orcamentos SET servico = ? WHERE id = ?', (n_valor,usuario))
            conexao.commit()
            print('Editado com sucesso ✅')
        case '4':
            cursor.execute('UPDATE orcamentos SET valor = ? WHERE id = ?', (n_valor,usuario))
            conexao.commit()
            print('Editado com sucesso ✅')
        case '5':
            cursor.execute('UPDATE orcamentos SET data = ? WHERE id = ?', (n_valor,usuario))
            conexao.commit()
            print('Editado com sucesso ✅')
        case _:
            print('Escolha uma das opções anteriores!')
def init():
    while True:
        print(f'''{'-'*50}Gerenciador do banco de dados{'-'*50}

📋 Menu
    1️⃣  Adicionar servicos
    2️⃣  Editar servicos
    3️⃣  Remover servicos
    4️⃣  Visualizar serviços
    5️⃣  Sair''')
        try:
            opcao = int(input('Digite uma das opções anteriores: '))
        except ValueError:
            print('Digite apenas números')
            continue
        match opcao:
            case 1:
                add()
            case 2:
                a = edit()
                if not a:
                    continue
            case 5:
                break
        break
