import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()


USUARIO = os.getenv('DB_USER', 'root')
SENHA   = os.getenv('DB_PASSWORD')
HOST    = os.getenv('DB_HOST', 'localhost')
BANCO   = os.getenv('DB_NAME', 'axis_finance')

if not SENHA:
    raise EnvironmentError("Variável DB_PASSWORD não definida. Configure o arquivo .env")


EXCEL_PATH = os.getenv('EXCEL_PATH', 'axis.xlsx')

print("=" * 45)
print("  AXIS FINANCE - ETL Excel → MySQL")
print("=" * 45)

print("\n[1/4] Conectando ao MySQL...")
engine = create_engine(f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}/{BANCO}")
print("      Conexão estabelecida.")

print("\n[2/4] Lendo arquivo Excel...")
df_revenue  = pd.read_excel(EXCEL_PATH, sheet_name='revenue')
df_expenses = pd.read_excel(EXCEL_PATH, sheet_name='expenses')
df_debts    = pd.read_excel(EXCEL_PATH, sheet_name='debts')
df_goals    = pd.read_excel(EXCEL_PATH, sheet_name='goals')
print(f"      Lido: {len(df_revenue)} receitas | {len(df_expenses)} despesas | "
      f"{len(df_debts)} dívidas | {len(df_goals)} metas")

print("\n[3/4] Limpando dados...")

for df in [df_revenue, df_expenses, df_debts, df_goals]:
    cols_to_drop = [c for c in df.columns if str(c).strip() == '' or str(c).isspace()]
    df.drop(columns=cols_to_drop, inplace=True)
print("      Colunas vazias removidas.")

print("\n[4/4] Enviando para o banco de dados...")
try:
    df_revenue.to_sql('revenue',   con=engine, if_exists='replace', index=False)
    df_expenses.to_sql('expenses', con=engine, if_exists='replace', index=False)
    df_debts.to_sql('debts',       con=engine, if_exists='replace', index=False)
    df_goals.to_sql('goals',       con=engine, if_exists='replace', index=False)
    print("      Dados carregados com sucesso.")
except Exception as e:
    print(f"      ERRO ao carregar dados: {e}")
    raise
finally:
    print("\n" + "=" * 45)
    print("  Processo finalizado.")
    print("=" * 45)
