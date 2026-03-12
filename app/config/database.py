import pyodbc


def get_connection():
    conexao = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=Papelaria_AmorPerfeito;"
        "Trusted_Connection=yes;"
    )
    return conexao