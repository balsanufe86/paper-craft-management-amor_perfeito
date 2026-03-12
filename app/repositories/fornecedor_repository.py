from app.config.database import get_connection


def listar_fornecedores():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_fornecedor, razao_nome, nome_fantasia, cpf_cnpj,
               telefone, email, endereco, cidade, estado, cep,
               contato_responsavel, observacoes, ativo
        FROM Fornecedores
        ORDER BY id_fornecedor
    """)

    fornecedores = cursor.fetchall()
    conexao.close()
    return fornecedores


def listar_fornecedores_ativos():
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_fornecedor, razao_nome, nome_fantasia, cpf_cnpj,
               telefone, email, endereco, cidade, estado, cep,
               contato_responsavel, observacoes, ativo
        FROM Fornecedores
        WHERE ativo = 1
        ORDER BY id_fornecedor
    """)

    fornecedores = cursor.fetchall()
    conexao.close()
    return fornecedores


def buscar_fornecedor_por_id(id_fornecedor):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_fornecedor, razao_nome, nome_fantasia, cpf_cnpj,
               telefone, email, endereco, cidade, estado, cep,
               contato_responsavel, observacoes, ativo
        FROM Fornecedores
        WHERE id_fornecedor = ?
    """, (id_fornecedor,))

    fornecedor = cursor.fetchone() 
    conexao.close()
    return fornecedor 


def inserir_fornecedor(razao_nome, nome_fantasia, cpf_cnpj, telefone, email,
                       endereco, cidade, estado, cep,
                       contato_responsavel, observacoes):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Fornecedores (
            razao_nome,
            nome_fantasia,
            cpf_cnpj,
            telefone,
            email,
            endereco,
            cidade,
            estado,
            cep,
            contato_responsavel,
            observacoes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        razao_nome,
        nome_fantasia,
        cpf_cnpj,
        telefone,
        email,
        endereco,
        cidade,
        estado,
        cep,
        contato_responsavel,
        observacoes
    ))

    conexao.commit() # Importante: commit para salvar as alterações no banco
    conexao.close()


def atualizar_fornecedor(id_fornecedor, razao_nome, nome_fantasia, cpf_cnpj,
                         telefone, email, endereco, cidade, estado, cep,
                         contato_responsavel, observacoes, ativo):

    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Fornecedores
        SET razao_nome = ?,
            nome_fantasia = ?,
            cpf_cnpj = ?,
            telefone = ?,
            email = ?,
            endereco = ?,
            cidade = ?,
            estado = ?,
            cep = ?,
            contato_responsavel = ?,
            observacoes = ?,
            ativo = ?
        WHERE id_fornecedor = ?
    """, (
        razao_nome,
        nome_fantasia,
        cpf_cnpj,
        telefone,
        email,
        endereco,
        cidade,
        estado,
        cep,
        contato_responsavel,
        observacoes,
        ativo,
        id_fornecedor
    ))

    conexao.commit()
    conexao.close()


def deletar_fornecedor(id_fornecedor):
    conexao = get_connection()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Fornecedores
        SET ativo = 0
        WHERE id_fornecedor = ?
    """, (id_fornecedor,))

    conexao.commit()
    conexao.close()