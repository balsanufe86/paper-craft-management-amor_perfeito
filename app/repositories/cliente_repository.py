from app.config.database import get_connection


def listar_clientes():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_cliente, nome, telefone, instagram, endereco,
               cidade, estado, cep, observacoes, data_cadastro, ativo
        FROM Clientes
        ORDER BY id_cliente
    """)

    clientes = cursor.fetchall()
    conexao.close()
    return clientes


def listar_clientes_ativos():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_cliente, nome, telefone, instagram, endereco,
               cidade, estado, cep, observacoes, data_cadastro, ativo
        FROM Clientes
        WHERE ativo = 1
        ORDER BY id_cliente
    """)

    clientes = cursor.fetchall()
    conexao.close()
    return clientes


def buscar_cliente_por_id(id_cliente):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_cliente, nome, telefone, instagram, endereco,
               cidade, estado, cep, observacoes, data_cadastro, ativo
        FROM Clientes
        WHERE id_cliente = ?
    """, (id_cliente,))

    cliente = cursor.fetchone()
    conexao.close()
    return cliente


def inserir_cliente(nome, telefone, instagram, endereco,
                    cidade, estado, cep, observacoes):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Clientes (
            nome, telefone, instagram, endereco,
            cidade, estado, cep, observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome, telefone, instagram, endereco,
        cidade, estado, cep, observacoes
    ))

    conexao.commit()
    conexao.close()


def atualizar_cliente(id_cliente, nome, telefone, instagram, endereco,
                      cidade, estado, cep, observacoes, ativo):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Clientes
        SET nome = ?,
            telefone = ?,
            instagram = ?,
            endereco = ?,
            cidade = ?,
            estado = ?,
            cep = ?,
            observacoes = ?,
            ativo = ?
        WHERE id_cliente = ?
    """, (
        nome, telefone, instagram, endereco,
        cidade, estado, cep, observacoes, ativo,
        id_cliente
    ))

    conexao.commit()
    conexao.close()


def deletar_cliente(id_cliente):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Clientes
        SET ativo = 0
        WHERE id_cliente = ?
    """, (id_cliente,))

    conexao.commit()
    conexao.close()