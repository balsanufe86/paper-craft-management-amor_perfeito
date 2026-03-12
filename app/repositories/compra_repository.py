from app.config.database import get_connection


def listar_compras():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_compra, id_fornecedor, data_compra, data_recebimento,
               valor_total, status_compra, observacoes
        FROM Compras
        ORDER BY id_compra
    """)

    compras = cursor.fetchall()
    conexao.close()
    return compras


def buscar_compra_por_id(id_compra):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_compra, id_fornecedor, data_compra, data_recebimento,
               valor_total, status_compra, observacoes
        FROM Compras
        WHERE id_compra = ?
    """, (id_compra,))

    compra = cursor.fetchone()
    conexao.close()
    return compra


def inserir_compra(id_fornecedor, status_compra, observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Compras (
            id_fornecedor,
            status_compra,
            observacoes
        )
        VALUES (?, ?, ?)
    """, (
        id_fornecedor,
        status_compra,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_compra(id_compra, id_fornecedor, data_recebimento,
                     valor_total, status_compra, observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Compras
        SET id_fornecedor = ?,
            data_recebimento = ?,
            valor_total = ?,
            status_compra = ?,
            observacoes = ?
        WHERE id_compra = ?
    """, (
        id_fornecedor,
        data_recebimento,
        valor_total,
        status_compra,
        observacoes,
        id_compra
    ))

    conexao.commit()
    conexao.close()


def deletar_compra(id_compra):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM Compras
        WHERE id_compra = ?
    """, (id_compra,))

    conexao.commit()
    conexao.close()