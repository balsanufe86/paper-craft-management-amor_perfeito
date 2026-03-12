from app.config.database import get_connection


def listar_pedidos():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pedido,
               id_cliente,
               data_pedido,
               data_entrega_prevista,
               data_entrega_real,
               status_pedido,
               tema_personalizacao,
               descricao_personalizacao,
               valor_produtos,
               valor_mao_obra,
               valor_frete,
               valor_desconto,
               valor_total,
               observacoes
        FROM Pedidos
        ORDER BY id_pedido
    """)

    pedidos = cursor.fetchall()
    conexao.close()

    return pedidos


def buscar_pedido_por_id(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pedido,
               id_cliente,
               data_pedido,
               data_entrega_prevista,
               data_entrega_real,
               status_pedido,
               tema_personalizacao,
               descricao_personalizacao,
               valor_produtos,
               valor_mao_obra,
               valor_frete,
               valor_desconto,
               valor_total,
               observacoes
        FROM Pedidos
        WHERE id_pedido = ?
    """, (id_pedido,))

    pedido = cursor.fetchone()
    conexao.close()

    return pedido


def listar_pedidos_por_cliente(id_cliente):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pedido,
               data_pedido,
               status_pedido,
               valor_total
        FROM Pedidos
        WHERE id_cliente = ?
        ORDER BY data_pedido DESC
    """, (id_cliente,))

    pedidos = cursor.fetchall()
    conexao.close()

    return pedidos


def inserir_pedido(id_cliente,
                   data_entrega_prevista,
                   status_pedido,
                   tema_personalizacao,
                   descricao_personalizacao,
                   observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Pedidos (
            id_cliente,
            data_entrega_prevista,
            status_pedido,
            tema_personalizacao,
            descricao_personalizacao,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        id_cliente,
        data_entrega_prevista,
        status_pedido,
        tema_personalizacao,
        descricao_personalizacao,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_pedido(id_pedido,
                     data_entrega_prevista,
                     data_entrega_real,
                     status_pedido,
                     tema_personalizacao,
                     descricao_personalizacao,
                     valor_produtos,
                     valor_mao_obra,
                     valor_frete,
                     valor_desconto,
                     valor_total,
                     observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Pedidos
        SET data_entrega_prevista = ?,
            data_entrega_real = ?,
            status_pedido = ?,
            tema_personalizacao = ?,
            descricao_personalizacao = ?,
            valor_produtos = ?,
            valor_mao_obra = ?,
            valor_frete = ?,
            valor_desconto = ?,
            valor_total = ?,
            observacoes = ?
        WHERE id_pedido = ?
    """, (
        data_entrega_prevista,
        data_entrega_real,
        status_pedido,
        tema_personalizacao,
        descricao_personalizacao,
        valor_produtos,
        valor_mao_obra,
        valor_frete,
        valor_desconto,
        valor_total,
        observacoes,
        id_pedido
    ))

    conexao.commit()
    conexao.close()


def deletar_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM Pedidos
        WHERE id_pedido = ?
    """, (id_pedido,))

    conexao.commit()
    conexao.close()