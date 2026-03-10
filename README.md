#  Axis Finance — Pipeline ETL Excel → MySQL → Power BI

Sistema de gestão financeira pessoal com pipeline de dados automatizado: extrai dados de planilhas Excel, transforma e carrega em banco MySQL, e alimenta dashboard no Power BI.

##  Arquitetura

```
axis.xlsx  →  axis_etl.py  →  MySQL (axis_finance)  →  Power BI
  (fonte)       (ETL Python)     (armazenamento)         (visualização)
```

##  Modelo de Dados

| Tabela | Descrição |
|--------|-----------|
| `revenue` | Receitas — salário, freelance, outros |
| `expenses` | Despesas com descrição e data |
| `debts` | Dívidas com credor e vencimento |
| `goals` | Metas financeiras de curto e longo prazo |

##  Stack

- **Python 3** — pandas, SQLAlchemy, python-dotenv
- **MySQL** — armazenamento relacional
- **Power BI** — visualização e dashboard
- **Excel** — fonte de entrada dos dados

##  Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/Ho-Cavalcanti/axis-finance.git
cd axis-finance
```

### 2. Instale as dependências
```bash
pip install pandas sqlalchemy pymysql python-dotenv openpyxl
```

### 3. Configure as variáveis de ambiente
```bash
# Renomeie o arquivo de exemplo e preencha suas credenciais
cp .env.example .env
```

### 4. Crie o banco de dados
```bash
mysql -u root -p < schema.sql
```

### 5. Execute o ETL
```bash
# Opção A — direto pelo Python
python axis_etl.py

# Opção B — pelo script automatizado (Windows)
etl.bat
```

O script `.bat` abre o Excel para edição, aguarda o fechamento e então executa o ETL automaticamente — basta clicar em "Atualizar" no Power BI ao final.

##  Estrutura do projeto

```
axis-finance/
├── axis_etl.py       # Script principal de ETL
├── schema.sql        # Definição do banco de dados
├── etl.bat           # Automação para Windows
├── .env.example      # Modelo de configuração
├── .gitignore        # Arquivos ignorados pelo Git
└── README.md
```

##  Decisões técnicas

- **Variáveis de ambiente** para credenciais — nenhuma senha exposta no código
- **`if_exists='replace'`** no carregamento — garante dados sempre atualizados
- **Limpeza automática** de colunas vazias antes do carregamento
- **Path relativo** para o Excel — funciona em qualquer máquina

## Autor

**Hoalison Cavalcanti**  
[github.com/Ho-Cavalcanti](https://github.com/Ho-Cavalcanti) · hoalisoncavalcanti@gmail.com
