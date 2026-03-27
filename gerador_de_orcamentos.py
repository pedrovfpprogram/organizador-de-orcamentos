from fpdf import FPDF
from manipulador_de_bd import salvar_dados, init
dados = salvar_dados()
print(f'''{'-'*50}Gerador de pdf de Orçamentos{'-'*50}
📋 Menu
    1️⃣  Gerar pdf
    2️⃣  Entrar no gerenciador de banco de dados''')
op = input("Escolha uma das opções anteriores: ")
match op:
    case "1":
        if not dados:
            print("Você não pode gerar um pdf sem ter dados no Banco de dados. Por favor, adicione orçamentos no banco de dados.")
        else:
            pass
    case '2':
        init()