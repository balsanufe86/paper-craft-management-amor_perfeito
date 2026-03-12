from app.config.database import get_connection


def testar_conexao():
    try:
        conexao = get_connection()
        cursor = conexao.cursor()
        cursor.execute("SELECT DB_NAME()")
        banco = cursor.fetchone()[0]
        print(f"Conectado com sucesso ao banco: {banco}")
        conexao.close()
    except Exception as erro:
        print(f"Erro ao conectar: {erro}")


if __name__ == "__main__":
    testar_conexao()