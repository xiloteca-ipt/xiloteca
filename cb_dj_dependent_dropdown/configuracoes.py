print("Importando pyodbc")
import pyodbc

print("Conectando")

dados_conexao = (
     "Driver={SQL Server};"
     "Server=SPON019400028\SQLEXPRESS;"
     "Database=Madeiras;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão funcionou")

cursor = conexao.cursor()
comando = "select * from madeira_ocorrencia"
print(cursor.execute(comando).fetchall())