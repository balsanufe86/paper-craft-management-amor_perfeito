from app.config.database import get_connection


def listar_consumos():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_consumo,
               id_pedido,
               id_item_pedido,
               id_material,
               quantidade_consumida,
               custo_unitario_material,
               custo_total_material,
               data_consumo,
               observacoes
        FROM ConsumoMateriaisPedido
        ORDER BY id_consumo
    """)

    consumos = cursor.fetchall()
    conexao.close()

    return consumos


def listar_consumos_por_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_consumo,
               id_item_pedido,
               id_material,
               quantidade_consumida,
               custo_unitario_material,
               custo_total_material,
               data_consumo,
               observacoes
        FROM ConsumoMateriaisPedido
        WHERE id_pedido = ?
    """, (id_pedido,))

    consumos = cursor.fetchall()
    conexao.close()

    return consumos


def buscar_consumo_por_id(id_consumo):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_consumo,
               id_pedido,
               id_item_pedido,
               id_material,
               quantidade_consumida,
               custo_unitario_material,
               custo_total_material,
               data_consumo,
               observacoes
        FROM ConsumoMateriaisPedido
        WHERE id_consumo = ?
    """, (id_consumo,))

    consumo = cursor.fetchone()
    conexao.close()

    return consumo


def inserir_consumo_material(id_pedido,
                             id_item_pedido,
                             id_material,
                             quantidade_consumida,
                             custo_unitario_material,
                             observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO ConsumoMateriaisPedido (
            id_pedido,
            id_item_pedido,
            id_material,
            quantidade_consumida,
            custo_unitario_material,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        id_pedido,
        id_item_pedido,
        id_material,
        quantidade_consumida,
        custo_unitario_material,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_consumo_material(id_consumo,
                               id_item_pedido,
                               id_material,
                               quantidade_consumida,
                               custo_unitario_material,
                               observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE ConsumoMateriaisPedido
        SET id_item_pedido = ?,
            id_material = ?,
            quantidade_consumida = ?,
            custo_unitario_material = ?,
            observacoes = ?
        WHERE id_consumo = ?
    """, (
        id_item_pedido,
        id_material,
        quantidade_consumida,
        custo_unitario_material,
        observacoes,
        id_consumo
    ))

    conexao.commit()
    conexao.close()


def deletar_consumo_material(id_consumo):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM ConsumoMateriaisPedido
        WHERE id_consumo = ?
    """, (id_consumo,))

    conexao.commit()
    conexao.close()