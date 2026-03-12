from app.repositories import estoque_movimentacao_repository
from app.repositories import material_repository
from app.services.exceptions.business_exception import BusinessException


TIPOS_MOVIMENTACAO_VALIDOS = {"ENTRADA", "SAIDA", "AJUSTE"}

ORIGENS_MOVIMENTACAO_VALIDAS = {
    "COMPRA",
    "CONSUMO_PEDIDO",
    "PERDA",
    "CORRECAO",
    "DEVOLUCAO"
}


def obter_material_or_fail(id_material):
    """
    Busca um material pelo ID.
    Se não existir, lança uma exceção de negócio.
    """

    material = material_repository.buscar_material_por_id(id_material)

    if material is None:
        raise BusinessException(
            message="Material não encontrado.",
            code="MATERIAL_NAO_ENCONTRADO"
        )

    return material


def validar_material_ativo(material):
    """
    Verifica se o material está ativo.
    Considerando a ordem das colunas do SELECT do repository:
    material[8] = ativo
    """

    if material[8] != 1:
        raise BusinessException(
            message="O material está inativo e não pode receber movimentações.",
            code="MATERIAL_INATIVO"
        )


def validar_quantidade(quantidade):
    """
    Garante que a quantidade informada seja maior que zero.
    """

    if quantidade is None:
        raise BusinessException(
            message="A quantidade deve ser informada.",
            code="QUANTIDADE_NAO_INFORMADA"
        )

    if quantidade <= 0:
        raise BusinessException(
            message="A quantidade deve ser maior que zero.",
            code="QUANTIDADE_INVALIDA"
        )


def validar_tipo_movimentacao(tipo_movimentacao):
    """
    Valida se o tipo de movimentação está entre os permitidos.
    """

    if tipo_movimentacao not in TIPOS_MOVIMENTACAO_VALIDOS:
        raise BusinessException(
            message=f"Tipo de movimentação inválido. Use um dos valores: {', '.join(TIPOS_MOVIMENTACAO_VALIDOS)}.",
            code="TIPO_MOVIMENTACAO_INVALIDO"
        )


def validar_origem_movimentacao(origem_movimentacao):
    """
    Valida se a origem da movimentação está entre as permitidas.
    """

    if origem_movimentacao not in ORIGENS_MOVIMENTACAO_VALIDAS:
        raise BusinessException(
            message=f"Origem de movimentação inválida. Use um dos valores: {', '.join(ORIGENS_MOVIMENTACAO_VALIDAS)}.",
            code="ORIGEM_MOVIMENTACAO_INVALIDA"
        )


def atualizar_quantidade_material(material, nova_quantidade):
    """
    Atualiza o campo quantidade_atual do material.
    Aproveita a função atualizar_material já existente no repository.
    """

    material_repository.atualizar_material(
        id_material=material[0],
        nome_material=material[1],
        descricao=material[2],
        unidade_medida=material[3],
        quantidade_atual=nova_quantidade,
        quantidade_minima=material[5],
        custo_medio=material[6],
        local_armazenamento=material[7],
        ativo=material[8]
    )


def registrar_entrada_material(id_material, quantidade, origem_movimentacao,
                               id_origem=None, observacoes=None):
    """
    Registra uma entrada de estoque.

    Regras:
    - material deve existir
    - material deve estar ativo
    - quantidade deve ser maior que zero
    - origem deve ser válida
    - gera movimentação do tipo ENTRADA
    - atualiza quantidade_atual em Materiais
    """

    validar_quantidade(quantidade)
    validar_origem_movimentacao(origem_movimentacao)

    material = obter_material_or_fail(id_material)
    validar_material_ativo(material)

    quantidade_atual = material[4]
    nova_quantidade = quantidade_atual + quantidade

    estoque_movimentacao_repository.inserir_movimentacao(
        id_material=id_material,
        tipo_movimentacao="ENTRADA",
        origem_movimentacao=origem_movimentacao,
        id_origem=id_origem,
        quantidade=quantidade,
        observacoes=observacoes
    )

    atualizar_quantidade_material(material, nova_quantidade)


def registrar_saida_material(id_material, quantidade, origem_movimentacao,
                             id_origem=None, observacoes=None):
    """
    Registra uma saída de estoque.

    Regras:
    - material deve existir
    - material deve estar ativo
    - quantidade deve ser maior que zero
    - origem deve ser válida
    - não pode sair mais do que existe em estoque
    - gera movimentação do tipo SAIDA
    - atualiza quantidade_atual em Materiais
    """

    validar_quantidade(quantidade)
    validar_origem_movimentacao(origem_movimentacao)

    material = obter_material_or_fail(id_material)
    validar_material_ativo(material)

    quantidade_atual = material[4]

    if quantidade > quantidade_atual:
        raise BusinessException(
            message="Estoque insuficiente para realizar a saída.",
            code="ESTOQUE_INSUFICIENTE"
        )

    nova_quantidade = quantidade_atual - quantidade

    estoque_movimentacao_repository.inserir_movimentacao(
        id_material=id_material,
        tipo_movimentacao="SAIDA",
        origem_movimentacao=origem_movimentacao,
        id_origem=id_origem,
        quantidade=quantidade,
        observacoes=observacoes
    )

    atualizar_quantidade_material(material, nova_quantidade)


def registrar_ajuste_material(id_material, quantidade, observacoes=None):
    """
    Registra um ajuste de estoque.

    Neste projeto, o ajuste será tratado como correção manual.
    Como a tabela exige origem_movimentacao, será usada a origem 'CORRECAO'.

    Regra adotada:
    - quantidade informada representa o novo saldo real do material
    - o service compara com o saldo atual
    - se o novo saldo for maior, registra AJUSTE
    - se o novo saldo for menor, registra AJUSTE
    - depois atualiza quantidade_atual com o valor informado
    """

    if quantidade is None:
        raise BusinessException(
            message="A quantidade do ajuste deve ser informada.",
            code="QUANTIDADE_AJUSTE_NAO_INFORMADA"
        )

    if quantidade < 0:
        raise BusinessException(
            message="A quantidade do ajuste não pode ser negativa.",
            code="QUANTIDADE_AJUSTE_INVALIDA"
        )

    material = obter_material_or_fail(id_material)
    validar_material_ativo(material)

    quantidade_atual = material[4]

    if quantidade == quantidade_atual:
        raise BusinessException(
            message="O valor informado para ajuste é igual ao estoque atual. Nenhuma alteração foi realizada.",
            code="AJUSTE_SEM_ALTERACAO"
        )

    diferenca = abs(quantidade - quantidade_atual)

    estoque_movimentacao_repository.inserir_movimentacao(
        id_material=id_material,
        tipo_movimentacao="AJUSTE",
        origem_movimentacao="CORRECAO",
        id_origem=None,
        quantidade=diferenca,
        observacoes=observacoes
    )

    atualizar_quantidade_material(material, quantidade)


def obter_quantidade_atual(id_material):
    """
    Retorna a quantidade atual do material com base na tabela Materiais.
    """

    material = obter_material_or_fail(id_material)
    return material[4]


def verificar_estoque_suficiente(id_material, quantidade):
    """
    Retorna True se houver estoque suficiente.
    Caso contrário, lança exceção.
    """

    validar_quantidade(quantidade)

    material = obter_material_or_fail(id_material)
    validar_material_ativo(material)

    quantidade_atual = material[4]

    if quantidade > quantidade_atual:
        raise BusinessException(
            message="Estoque insuficiente para a quantidade solicitada.",
            code="ESTOQUE_INSUFICIENTE"
        )

    return True


def listar_movimentacoes():
    """
    Lista todas as movimentações de estoque.
    """

    return estoque_movimentacao_repository.listar_movimentacoes()


def listar_movimentacoes_por_material(id_material):
    """
    Lista as movimentações de um material específico.
    """

    obter_material_or_fail(id_material)
    return estoque_movimentacao_repository.listar_movimentacoes_por_material(id_material)