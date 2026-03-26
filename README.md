# 📄 Organizador de Orçamentos em Python (v0.1)

Um sistema modular para gerenciar serviços e gerar relatórios em PDF, utilizando **SQLite3** para persistência e **FPDF** para documentos.

---

## 🚀 Funcionalidades da Versão 0.1
- [x] **Banco de Dados Local:** Persistência automática via SQLite.
- [x] **CRUD Modular:** Separação entre lógica de banco (`manipulador_de_bd.py`) e interface (`gerador_de_orcamentos.py`).
- [x] **Prevenção de Erros:** Tratamento de entradas inválidas com `try/except`.
- [x] **Interface via Terminal:** Menu interativo e intuitivo.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.14.3**
* **SQLite3** (Nativo)
* **FPDF** (Geração de PDF)

---

## 📋 Passo a Passo para Execução

### 1. Clonar o Repositório
Abra o terminal e clone o projeto:
```bash
git clone [https://github.com/pedrovfpprogram/organizador-de-orcamentos.git](https://github.com/pedrovfpprogram/organizador-de-orcamentos.git)
cd organizador-de-orcamentos
