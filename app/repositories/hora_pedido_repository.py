from app.config.database import get_connection


def listar_horas_pedido():

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_hora_pedido,
               id_pedido,
               data_registro,
               tipo_atividade,
               horas_gastas,
               custo_hora,
               valor_total_horas,
               observacoes
        FROM HorasPedido
        ORDER BY id_hora_pedido
    """)

    horas = cursor.fetchall()
    conexao.close()

    return horas


def listar_horas_por_pedido(id_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_hora_pedido,
               data_registro,
               tipo_atividade,
               horas_gastas,
               custo_hora,
               valor_total_horas,
               observacoes
        FROM HorasPedido
        WHERE id_pedido = ?
    """, (id_pedido,))

    horas = cursor.fetchall()
    conexao.close()

    return horas


def buscar_hora_por_id(id_hora_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_hora_pedido,
               id_pedido,
               data_registro,
               tipo_atividade,
               horas_gastas,
               custo_hora,
               valor_total_horas,
               observacoes
        FROM HorasPedido
        WHERE id_hora_pedido = ?
    """, (id_hora_pedido,))

    hora = cursor.fetchone()
    conexao.close()

    return hora


def inserir_hora_pedido(id_pedido,
                        tipo_atividade,
                        horas_gastas,
                        custo_hora,
                        observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO HorasPedido (
            id_pedido,
            tipo_atividade,
            horas_gastas,
            custo_hora,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        id_pedido,
        tipo_atividade,
        horas_gastas,
        custo_hora,
        observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_hora_pedido(id_hora_pedido,
                          tipo_atividade,
                          horas_gastas,
                          custo_hora,
                          observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE HorasPedido
        SET tipo_atividade = ?,
            horas_gastas = ?,
            custo_hora = ?,
            observacoes = ?
        WHERE id_hora_pedido = ?
    """, (
        tipo_atividade,
        horas_gastas,
        custo_hora,
        observacoes,
        id_hora_pedido
    ))

    conexao.commit()
    conexao.close()


def deletar_hora_pedido(id_hora_pedido):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM HorasPedido
        WHERE id_hora_pedido = ?
    """, (id_hora_pedido,))

    conexao.commit()
    conexao.close()