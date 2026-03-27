📄 Organizador de Orçamentos em Python (v0.1)
Um sistema modular para gerenciar serviços e gerar relatórios em PDF, utilizando SQLite3 para persistência e FPDF para documentos.

🚀 Funcionalidades da Versão 0.1
[x] Banco de Dados Local: Persistência automática via SQLite.

[x] CRUD Modular: Separação entre lógica de banco (manipulador_de_bd.py) e interface (gerador_de_orcamentos.py).

[x] Prevenção de Erros: Tratamento de entradas inválidas com try/except.

[x] Interface via Terminal: Menu interativo e intuitivo.

🛠️ Tecnologias Utilizadas
Python 3.14.3

SQLite3 (Nativo)

FPDF (Geração de PDF)

📋 Passo a Passo para Execução
1. Clonar o Repositório
Abra o terminal e clone o projeto:

Bash
git clone https://github.com/pedrovfpprogram/organizador-de-orcamentos.git
cd organizador-de-orcamentos
2. Instalar Dependências
Certifique-se de ter o Python 3.14.3 instalado. Instale a biblioteca necessária para os PDFs:

Bash
pip install fpdf
3. Rodar o Sistema
Para iniciar o gerenciador de orçamentos, execute o arquivo principal:

Bash
python gerador_de_orcamentos.py
4. Usar o Menu
Selecione a opção 1 para cadastrar um novo cliente e serviço.

O banco de dados orcamentos.db será criado automaticamente na primeira vez.

Para gerar o relatório final, utilize a integração com o módulo de PDF (funcionalidade em expansão na v0.2).

📂 Estrutura de Arquivos
gerador_de_orcamentos.py: Script principal (Interface do usuário).

manipulador_de_bd.py: Módulo de funções do banco de dados (SQLite).

orcamentos.db: Arquivo onde seus dados ficam salvos com segurança.

📌 Roadmap (v0.2)
[ ] Ativação da exportação individual para PDF.

[ ] Função de busca avançada por ID ou Nome.

[ ] Formatação de cores e logotipos nos orçamentos gerados.

⚖️ Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE.

Desenvolvido por Pedro como portfólio técnico.
