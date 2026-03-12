from app.config.database import get_connection


def listar_materiais():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_material, nome_material, descricao, unidade_medida,
               quantidade_atual, quantidade_minima, custo_medio,
               local_armazenamento, ativo
        FROM Materiais
        ORDER BY id_material
    """)

    materiais = cursor.fetchall()
    conexao.close()
    return materiais


def listar_materiais_ativos():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_material, nome_material, descricao, unidade_medida,
               quantidade_atual, quantidade_minima, custo_medio,
               local_armazenamento, ativo
        FROM Materiais
        WHERE ativo = 1
        ORDER BY id_material
    """)

    materiais = cursor.fetchall()
    conexao.close()
    return materiais


def buscar_material_por_id(id_material):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_material, nome_material, descricao, unidade_medida,
               quantidade_atual, quantidade_minima, custo_medio,
               local_armazenamento, ativo
        FROM Materiais
        WHERE id_material = ?
    """, (id_material,))

    material = cursor.fetchone()
    conexao.close()
    return material


def inserir_material(nome_material, descricao, unidade_medida,
                     quantidade_atual, quantidade_minima,
                     custo_medio, local_armazenamento):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Materiais (
            nome_material,
            descricao,
            unidade_medida,
            quantidade_atual,
            quantidade_minima,
            custo_medio,
            local_armazenamento
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nome_material,
        descricao,
        unidade_medida,
        quantidade_atual,
        quantidade_minima,
        custo_medio,
        local_armazenamento
    ))

    conexao.commit()
    conexao.close()


def atualizar_material(id_material, nome_material, descricao, unidade_medida,
                       quantidade_atual, quantidade_minima,
                       custo_medio, local_armazenamento, ativo):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Materiais
        SET nome_material = ?,
            descricao = ?,
            unidade_medida = ?,
            quantidade_atual = ?,
            quantidade_minima = ?,
            custo_medio = ?,
            local_armazenamento = ?,
            ativo = ?
        WHERE id_material = ?
    """, (
        nome_material,
        descricao,
        unidade_medida,
        quantidade_atual,
        quantidade_minima,
        custo_medio,
        local_armazenamento,
        ativo,
        id_material
    ))

    conexao.commit()
    conexao.close()


def deletar_material(id_material):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Materiais
        SET ativo = 0
        WHERE id_material = ?
    """, (id_material,))

    conexao.commit()
    conexao.close()