# 📄 Organizador de Orçamentos em Python (v0.1)

Um sistema modular para gerenciar serviços e gerar relatórios em PDF, utilizando **SQLite3** para persistência e **FPDF** para documentos.

---

## 🚀 Funcionalidades da Versão 0.1

- [x] **Banco de Dados Local**  
  Persistência automática via SQLite.

- [x] **CRUD Modular**  
  Separação entre lógica de banco (`manipulador_de_bd.py`) e interface (`gerador_de_orcamentos.py`).

- [x] **Prevenção de Erros**  
  Tratamento de entradas inválidas com `try/except`.

- [x] **Interface via Terminal**  
  Menu interativo e intuitivo.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.14.3  
- SQLite3 (nativo)  
- FPDF (geração de PDF)

---

## 📋 Passo a Passo para Execução

### 1. Clonar o Repositório

Abra o terminal e execute:

```bash
git clone https://github.com/pedrovfpprogram/organizador-de-orcamentos.git
cd organizador-de-orcamentos
```
### 2. Instalar Dependências

Certifique-se de ter o Python 3.14.3 instalado.

Instale a biblioteca necessária:
```bash
pip install fpdf
```
### 3. Rodar o Sistema

Execute o arquivo principal:

```bash
python gerador_de_orcamentos.py
```
### 4. Usar o Menu

Selecione a opção 1 para cadastrar um novo cliente e serviço

O banco de dados orcamentos.db será criado automaticamente na primeira execução

Para gerar o relatório final, utilize a integração com PDF (funcionalidade em expansão na v0.2)

---

## 📂 Estruturas de arquivos

📁 organizador-de-orcamentos

├── gerador_de_orcamentos.py   # Interface do usuário

├── manipulador_de_bd.py       # Funções do banco de dados (SQLite)

├── orcamentos.db              # Banco de dados local (Criado automaticamente)

---

## 📌 Roadmap (v0.2)

 Exportação individual para PDF
 
 Busca avançada por ID ou Nome
 
 Personalização com cores e logotipo nos orçamentos

---
 
## ⚖️ Licença

Este projeto está sob a licença MIT.

Veja o arquivo LICENSE para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por Pedro como portfólio técnico.

---
