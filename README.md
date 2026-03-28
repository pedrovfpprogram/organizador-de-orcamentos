# 📄 Organizador de Orçamentos em Python (v0.1)

Um sistema modular para gerenciar serviços e gerar relatórios em PDF, utilizando **SQLite3** para persistência e **FPDF** para documentos.

---

## 🚀 Funcionalidades da Versão 0.2
- [x] **Banco de Dados Local:** Persistência automática via SQLite.
- [x] **CRUD Modular:** Separação entre lógica de banco (`manipulador_de_bd.py`) e interface (`gerador_de_orcamentos.py`).
- [x] **Interface via Terminal:** Menu interativo para geração de PDF e gestão de dados.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.14.3**
* **SQLite3** (Nativo)
* **FPDF** (Geração de PDF)

---

## 📋 Passo a Passo para Execução

### 1. Baixar o Projeto
1. Acesse o repositório no GitHub.
2. Clique no botão verde **Code** e selecione **Download ZIP**.
3. Extraia os arquivos em uma pasta no seu computador.

### 2. Instalar Dependências
Certifique-se de ter o Python instalado. Abra o terminal na pasta do projeto e instale a biblioteca de PDF:
```bash
pip install fpdf
```
### 3. Rodar o Sistema
Para iniciar o gerenciador, execute o arquivo principal:

```bash
python gerador_de_orcamentos.py
```
### 4. Como Usar o Menu
Opção 1 (Gerar PDF): Cria o documento PDF com base nos dados salvos no banco.

Opção 2 (Gerenciador): Abre o submenu para gerenciar o banco de dados.

Cadastrar Dados: Dentro da Opção 2, selecione 1 para inserir Nome, Contato, Serviço, Valor e Data.

Persistência: O arquivo orcamentos.db será criado automaticamente na primeira vez que você salvar um dado.

---

## 📂 Estrutura de Arquivos
gerador_de_orcamentos.py: Interface principal e lógica de exportação.

manipulador_de_bd.py: Módulo de funções para conexão e salvamento no SQLite.

orcamentos.db: Onde seus dados ficam armazenados (gerado via script).

---

## ⚖️ Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE.

---

*Desenvolvido por Pedro como portfólio técnico.*

---
