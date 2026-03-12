from app.config.database import get_connection


def listar_itens_compra():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_compra,
               id_compra,
               id_material,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensCompra
        ORDER BY id_item_compra
    """)

    itens = cursor.fetchall()
    conexao.close()

    return itens


def listar_itens_por_compra(id_compra):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_compra,
               id_compra,
               id_material,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensCompra
        WHERE id_compra = ?
    """, (id_compra,))

    itens = cursor.fetchall()
    conexao.close()

    return itens


def buscar_item_por_id(id_item_compra):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_item_compra,
               id_compra,
               id_material,
               quantidade,
               valor_unitario,
               valor_total_item
        FROM ItensCompra
        WHERE id_item_compra = ?
    """, (id_item_compra,))

    item = cursor.fetchone()
    conexao.close()

    return item


def inserir_item_compra(id_compra, id_material, quantidade, valor_unitario):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO ItensCompra (
            id_compra,
            id_material,
            quantidade,
            valor_unitario
        )
        VALUES (?, ?, ?, ?)
    """, (
        id_compra,
        id_material,
        quantidade,
        valor_unitario
    ))

    conexao.commit()
    conexao.close()


def atualizar_item_compra(id_item_compra, id_material, quantidade, valor_unitario):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE ItensCompra
        SET id_material = ?,
            quantidade = ?,
            valor_unitario = ?
        WHERE id_item_compra = ?
    """, (
        id_material,
        quantidade,
        valor_unitario,
        id_item_compra
    ))

    conexao.commit()
    conexao.close()


def deletar_item_compra(id_item_compra):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM ItensCompra
        WHERE id_item_compra = ?
    """, (id_item_compra,))

    conexao.commit()
    conexao.close()