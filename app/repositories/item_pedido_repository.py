from app.config.database import get_connection


def listar_itens_pedido():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_pedido,
               id_pedido,
               id_produto,
               descricao_item_personalizado,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensPedido
        ORDER BY id_item_pedido
    """)

    itens = cursor.fetchall()
    conexao.close()

    return itens


def listar_itens_por_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_pedido,
               id_pedido,
               id_produto,
               descricao_item_personalizado,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensPedido
        WHERE id_pedido = ?
    """, (id_pedido,))

    itens = cursor.fetchall()
    conexao.close()

    return itens


def buscar_item_por_id(id_item_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_pedido,
               id_pedido,
               id_produto,
               descricao_item_personalizado,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensPedido
        WHERE id_item_pedido = ?
    """, (id_item_pedido,))

    item = cursor.fetchone()
    conexao.close()

    return item


def inserir_item_pedido(id_pedido,
                        id_produto,
                        descricao_item_personalizado,
                        quantidade,
                        valor_unitario):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO ItensPedido (
            id_pedido,
            id_produto,
            descricao_item_personalizado,
            quantidade,
            valor_unitario
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        id_pedido,
        id_produto,
        descricao_item_personalizado,
        quantidade,
        valor_unitario
    ))

    conexao.commit()
    conexao.close()


def atualizar_item_pedido(id_item_pedido,
                          id_produto,
                          descricao_item_personalizado,
                          quantidade,
                          valor_unitario):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE ItensPedido
        SET id_produto = ?,
            descricao_item_personalizado = ?,
            quantidade = ?,
            valor_unitario = ?
        WHERE id_item_pedido = ?
    """, (
        id_produto,
        descricao_item_personalizado,
        quantidade,
        valor_unitario,
        id_item_pedido
    ))

    conexao.commit()
    conexao.close()


def deletar_item_pedido(id_item_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM ItensPedido
        WHERE id_item_pedido = ?
    """, (id_item_pedido,))

    conexao.commit()
    conexao.close()