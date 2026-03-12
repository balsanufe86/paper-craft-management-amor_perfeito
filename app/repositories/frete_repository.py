from app.config.database import get_connection


def listar_fretes():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_frete,
               id_pedido,
               tipo_frete,
               valor_frete,
               custo_frete,
               endereco_entrega,
               data_envio,
               data_entrega,
               status_frete,
               codigo_rastreio,
               observacoes
        FROM Fretes
        ORDER BY id_frete
    """)

    fretes = cursor.fetchall()
    conexao.close()

    return fretes


def listar_fretes_por_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_frete,
               tipo_frete,
               valor_frete,
               custo_frete,
               endereco_entrega,
               data_envio,
               data_entrega,
               status_frete,
               codigo_rastreio,
               observacoes
        FROM Fretes
        WHERE id_pedido = ?
    """, (id_pedido,))

    fretes = cursor.fetchall()
    conexao.close()

    return fretes


def buscar_frete_por_id(id_frete):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_frete,
               id_pedido,
               tipo_frete,
               valor_frete,
               custo_frete,
               endereco_entrega,
               data_envio,
               data_entrega,
               status_frete,
               codigo_rastreio,
               observacoes
        FROM Fretes
        WHERE id_frete = ?
    """, (id_frete,))

    frete = cursor.fetchone()
    conexao.close()

    return frete


def inserir_frete(id_pedido,
                  tipo_frete,
                  valor_frete,
                  custo_frete,
                  endereco_entrega,
                  data_envio,
                  data_entrega,
                  status_frete,
                  codigo_rastreio,
                  observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Fretes (
            id_pedido,
            tipo_frete,
            valor_frete,
            custo_frete,
            endereco_entrega,
            data_envio,
            data_entrega,
            status_frete,
            codigo_rastreio,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        id_pedido,
        tipo_frete,
        valor_frete,
        custo_frete,
        endereco_entrega,
        data_envio,
        data_entrega,
        status_frete,
        codigo_rastreio,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_frete(id_frete,
                    tipo_frete,
                    valor_frete,
                    custo_frete,
                    endereco_entrega,
                    data_envio,
                    data_entrega,
                    status_frete,
                    codigo_rastreio,
                    observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Fretes
        SET tipo_frete = ?,
            valor_frete = ?,
            custo_frete = ?,
            endereco_entrega = ?,
            data_envio = ?,
            data_entrega = ?,
            status_frete = ?,
            codigo_rastreio = ?,
            observacoes = ?
        WHERE id_frete = ?
    """, (
        tipo_frete,
        valor_frete,
        custo_frete,
        endereco_entrega,
        data_envio,
        data_entrega,
        status_frete,
        codigo_rastreio,
        observacoes,
        id_frete
    ))

    conexao.commit()
    conexao.close()


def deletar_frete(id_frete):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM Fretes
        WHERE id_frete = ?
    """, (id_frete,))

    conexao.commit()
    conexao.close()