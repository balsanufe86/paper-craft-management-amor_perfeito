from app.config.database import get_connection


def listar_movimentacoes():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_movimentacao,
               id_material,
               tipo_movimentacao,
               origem_movimentacao,
               id_origem,
               quantidade,
               data_movimentacao,
               observacoes
        FROM EstoqueMovimentacoes
        ORDER BY id_movimentacao
    """)

    movimentacoes = cursor.fetchall()
    conexao.close()

    return movimentacoes


def listar_movimentacoes_por_material(id_material):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_movimentacao,
               tipo_movimentacao,
               origem_movimentacao,
               id_origem,
               quantidade,
               data_movimentacao,
               observacoes
        FROM EstoqueMovimentacoes
        WHERE id_material = ?
        ORDER BY data_movimentacao
    """, (id_material,))

    movimentacoes = cursor.fetchall()
    conexao.close()

    return movimentacoes


def buscar_movimentacao_por_id(id_movimentacao):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_movimentacao,
               id_material,
               tipo_movimentacao,
               origem_movimentacao,
               id_origem,
               quantidade,
               data_movimentacao,
               observacoes
        FROM EstoqueMovimentacoes
        WHERE id_movimentacao = ?
    """, (id_movimentacao,))

    movimentacao = cursor.fetchone()
    conexao.close()

    return movimentacao


def inserir_movimentacao(id_material,
                         tipo_movimentacao,
                         origem_movimentacao,
                         id_origem,
                         quantidade,
                         observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO EstoqueMovimentacoes (
            id_material,
            tipo_movimentacao,
            origem_movimentacao,
            id_origem,
            quantidade,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        id_material,
        tipo_movimentacao,
        origem_movimentacao,
        id_origem,
        quantidade,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def deletar_movimentacao(id_movimentacao):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM EstoqueMovimentacoes
        WHERE id_movimentacao = ?
    """, (id_movimentacao,))

    conexao.commit()
    conexao.close()