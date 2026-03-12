from app.config.database import get_connection


def listar_produtos():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, nome_produto, descricao, categoria, preco_base,
               tipo_produto, usa_materiais, controla_estoque, ativo
        FROM Produtos
        ORDER BY id_produto
    """)

    produtos = cursor.fetchall()
    conexao.close()
    return produtos


def listar_produtos_ativos():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, nome_produto, descricao, categoria, preco_base,
               tipo_produto, usa_materiais, controla_estoque, ativo
        FROM Produtos
        WHERE ativo = 1
        ORDER BY id_produto
    """)

    produtos = cursor.fetchall()
    conexao.close()
    return produtos


def buscar_produto_por_id(id_produto):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, nome_produto, descricao, categoria, preco_base,
               tipo_produto, usa_materiais, controla_estoque, ativo
        FROM Produtos
        WHERE id_produto = ?
    """, (id_produto,))

    produto = cursor.fetchone()
    conexao.close()
    return produto


def inserir_produto(nome_produto, descricao, categoria, preco_base,
                    tipo_produto, usa_materiais, controla_estoque, ativo):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Produtos (
            nome_produto, descricao, categoria, preco_base,
            tipo_produto, usa_materiais, controla_estoque, ativo
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome_produto, descricao, categoria, preco_base,
        tipo_produto, usa_materiais, controla_estoque, ativo
    ))

    conexao.commit()
    conexao.close()


def atualizar_produto(id_produto, nome_produto, descricao, categoria, preco_base,
                      tipo_produto, usa_materiais, controla_estoque, ativo):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Produtos
        SET nome_produto = ?,
            descricao = ?,
            categoria = ?,
            preco_base = ?,
            tipo_produto = ?,
            usa_materiais = ?,
            controla_estoque = ?,
            ativo = ?
        WHERE id_produto = ?
    """, (
        nome_produto, descricao, categoria, preco_base,
        tipo_produto, usa_materiais, controla_estoque, ativo,
        id_produto
    ))

    conexao.commit()
    conexao.close()


def deletar_produto(id_produto):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Produtos
        SET ativo = 0
        WHERE id_produto = ?
    """, (id_produto,))

    conexao.commit()
    conexao.close()