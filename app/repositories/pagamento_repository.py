from app.config.database import get_connection


def listar_pagamentos():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pagamento,
               id_pedido,
               data_pagamento,
               valor_pago,
               forma_pagamento,
               status_pagamento,
               observacoes
        FROM Pagamentos
        ORDER BY id_pagamento
    """)

    pagamentos = cursor.fetchall()
    conexao.close()

    return pagamentos


def listar_pagamentos_por_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pagamento,
               data_pagamento,
               valor_pago,
               forma_pagamento,
               status_pagamento,
               observacoes
        FROM Pagamentos
        WHERE id_pedido = ?
        ORDER BY data_pagamento
    """, (id_pedido,))

    pagamentos = cursor.fetchall()
    conexao.close()

    return pagamentos


def buscar_pagamento_por_id(id_pagamento):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_pagamento,
               id_pedido,
               data_pagamento,
               valor_pago,
               forma_pagamento,
               status_pagamento,
               observacoes
        FROM Pagamentos
        WHERE id_pagamento = ?
    """, (id_pagamento,))

    pagamento = cursor.fetchone()
    conexao.close()

    return pagamento


def inserir_pagamento(id_pedido,
                      data_pagamento,
                      valor_pago,
                      forma_pagamento,
                      status_pagamento,
                      observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Pagamentos (
            id_pedido,
            data_pagamento,
            valor_pago,
            forma_pagamento,
            status_pagamento,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        id_pedido,
        data_pagamento,
        valor_pago,
        forma_pagamento,
        status_pagamento,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_pagamento(id_pagamento,
                        data_pagamento,
                        valor_pago,
                        forma_pagamento,
                        status_pagamento,
                        observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Pagamentos
        SET data_pagamento = ?,
            valor_pago = ?,
            forma_pagamento = ?,
            status_pagamento = ?,
            observacoes = ?
        WHERE id_pagamento = ?
    """, (
        data_pagamento,
        valor_pago,
        forma_pagamento,
        status_pagamento,
        observacoes,
        id_pagamento
    ))

    conexao.commit()
    conexao.close()


def deletar_pagamento(id_pagamento):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM Pagamentos
        WHERE id_pagamento = ?
    """, (id_pagamento,))

    conexao.commit()
    conexao.close()