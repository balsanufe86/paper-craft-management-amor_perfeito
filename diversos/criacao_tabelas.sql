-- =========================================
-- SISTEMA PAPELARIA PERSONALIZADA
-- SCRIPT DE CRIAÇÃO DAS TABELAS
-- SQL SERVER

USE Papelaria_AmorPerfeito;
GO

-- =========================================
-- 1. CLIENTES
-- =========================================
CREATE TABLE Clientes (
    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(150) NOT NULL,
    telefone NVARCHAR(20) NULL,
    instagram NVARCHAR(100) NULL,
    endereco NVARCHAR(200) NULL,
    cidade NVARCHAR(100) NULL,
    estado NVARCHAR(50) NULL,
    cep NVARCHAR(10) NULL,
    observacoes NVARCHAR(500) NULL,
    data_cadastro DATETIME NOT NULL DEFAULT GETDATE(), -- default getdate preenche automaticamente com a data do cadastro
    ativo BIT NOT NULL DEFAULT 1 -- 1 ATIVO
);
GO

-- =========================================
-- 2. PRODUTOS
-- =========================================
CREATE TABLE Produtos (
    id_produto INT IDENTITY(1,1) PRIMARY KEY,
    nome_produto NVARCHAR(150) NOT NULL,
    descricao NVARCHAR(500) NULL,
    categoria NVARCHAR(100) NULL,
    preco_base DECIMAL(10,2) NOT NULL DEFAULT 0,
    tipo_produto NVARCHAR(30) NOT NULL,
    usa_materiais BIT NOT NULL DEFAULT 1,
    controla_estoque BIT NOT NULL DEFAULT 0, -- itens a observar o estoque 
    ativo BIT NOT NULL DEFAULT 1,
    CONSTRAINT CK_Produtos_TipoProduto
        CHECK (tipo_produto IN ('PRONTA_ENTREGA', 'PERSONALIZADO'))
);
GO

-- =========================================
-- 3. MATERIAIS
-- =========================================
CREATE TABLE Materiais (
    id_material INT IDENTITY(1,1) PRIMARY KEY,
    nome_material NVARCHAR(150) NOT NULL,
    descricao NVARCHAR(500) NULL,
    unidade_medida NVARCHAR(30) NOT NULL,
    quantidade_atual DECIMAL(18,4) NOT NULL DEFAULT 0,
    quantidade_minima DECIMAL(18,4) NOT NULL DEFAULT 0,
    custo_medio DECIMAL(12,4) NOT NULL DEFAULT 0,
    local_armazenamento NVARCHAR(100) NULL,
    ativo BIT NOT NULL DEFAULT 1
);
GO

-- =========================================
-- 4. FORNECEDORES
-- =========================================
CREATE TABLE Fornecedores (
    id_fornecedor INT IDENTITY(1,1) PRIMARY KEY,
    razao_nome NVARCHAR(150) NOT NULL,
    nome_fantasia NVARCHAR(150) NULL,
    cpf_cnpj NVARCHAR(20) NULL,
    telefone NVARCHAR(20) NULL,
    email NVARCHAR(150) NULL,
    endereco NVARCHAR(200) NULL,
    cidade NVARCHAR(100) NULL,
    estado NVARCHAR(50) NULL,
    cep NVARCHAR(10) NULL,
    contato_responsavel NVARCHAR(100) NULL,
    observacoes NVARCHAR(500) NULL,
    ativo BIT NOT NULL DEFAULT 1
);
GO

-- =========================================
-- 5. COMPRAS
-- =========================================
CREATE TABLE Compras (
    id_compra INT IDENTITY(1,1) PRIMARY KEY,
    id_fornecedor INT NOT NULL,
    data_compra DATETIME NOT NULL DEFAULT GETDATE(),
    data_recebimento DATETIME NULL,
    valor_total DECIMAL(12,2) NOT NULL DEFAULT 0,
    status_compra NVARCHAR(20) NOT NULL,
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_Compras_Fornecedores
        FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores(id_fornecedor),
    CONSTRAINT CK_Compras_StatusCompra
        CHECK (status_compra IN ('PENDENTE', 'RECEBIDA', 'CANCELADA', 'PARCIAL'))
);
GO

-- =========================================
-- 6. ITENS COMPRA
-- =========================================
CREATE TABLE ItensCompra (
    id_item_compra INT IDENTITY(1,1) PRIMARY KEY,
    id_compra INT NOT NULL,
    id_material INT NOT NULL,
    quantidade DECIMAL(18,4) NOT NULL,
    valor_unitario DECIMAL(12,4) NOT NULL,
    valor_total_item AS (quantidade * valor_unitario) PERSISTED,
    CONSTRAINT FK_ItensCompra_Compras
        FOREIGN KEY (id_compra) REFERENCES Compras(id_compra),
    CONSTRAINT FK_ItensCompra_Materiais
        FOREIGN KEY (id_material) REFERENCES Materiais(id_material),
    CONSTRAINT CK_ItensCompra_Quantidade
        CHECK (quantidade > 0),
    CONSTRAINT CK_ItensCompra_ValorUnitario
        CHECK (valor_unitario >= 0)
);
GO

-- =========================================
-- 7. PEDIDOS
-- =========================================
CREATE TABLE Pedidos (
    id_pedido INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT GETDATE(),
    data_entrega_prevista DATETIME NULL,
    data_entrega_real DATETIME NULL,
    status_pedido NVARCHAR(20) NOT NULL,
    tema_personalizacao NVARCHAR(150) NULL,
    descricao_personalizacao NVARCHAR(1000) NULL,
    valor_produtos DECIMAL(12,2) NOT NULL DEFAULT 0,
    valor_mao_obra DECIMAL(12,2) NOT NULL DEFAULT 0,
    valor_frete DECIMAL(12,2) NOT NULL DEFAULT 0,
    valor_desconto DECIMAL(12,2) NOT NULL DEFAULT 0,
    valor_total DECIMAL(12,2) NOT NULL DEFAULT 0,
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_Pedidos_Clientes
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    CONSTRAINT CK_Pedidos_StatusPedido
        CHECK (status_pedido IN ('ORCAMENTO', 'APROVADO', 'EM_PRODUCAO', 'FINALIZADO', 'ENTREGUE', 'CANCELADO'))
);
GO

-- =========================================
-- 8. ITENS PEDIDO
-- =========================================
CREATE TABLE ItensPedido (
    id_item_pedido INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    descricao_item_personalizado NVARCHAR(500) NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(12,2) NOT NULL,
    valor_total_item AS (quantidade * valor_unitario) PERSISTED,
    CONSTRAINT FK_ItensPedido_Pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    CONSTRAINT FK_ItensPedido_Produtos
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto),
    CONSTRAINT CK_ItensPedido_Quantidade
        CHECK (quantidade > 0),
    CONSTRAINT CK_ItensPedido_ValorUnitario
        CHECK (valor_unitario >= 0)
);
GO

-- =========================================
-- 9. CONSUMO DE MATERIAIS POR PEDIDO
-- =========================================
CREATE TABLE ConsumoMateriaisPedido (
    id_consumo INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_item_pedido INT NULL,
    id_material INT NOT NULL,
    quantidade_consumida DECIMAL(18,4) NOT NULL,
    custo_unitario_material DECIMAL(12,4) NOT NULL,
    custo_total_material AS (quantidade_consumida * custo_unitario_material) PERSISTED,
    data_consumo DATETIME NOT NULL DEFAULT GETDATE(),
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_ConsumoMateriaisPedido_Pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    CONSTRAINT FK_ConsumoMateriaisPedido_ItensPedido
        FOREIGN KEY (id_item_pedido) REFERENCES ItensPedido(id_item_pedido),
    CONSTRAINT FK_ConsumoMateriaisPedido_Materiais
        FOREIGN KEY (id_material) REFERENCES Materiais(id_material),
    CONSTRAINT CK_ConsumoMateriaisPedido_Quantidade
        CHECK (quantidade_consumida > 0),
    CONSTRAINT CK_ConsumoMateriaisPedido_CustoUnitario
        CHECK (custo_unitario_material >= 0)
);
GO

-- =========================================
-- 10. HORAS POR PEDIDO
-- =========================================
CREATE TABLE HorasPedido (
    id_hora_pedido INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    data_registro DATETIME NOT NULL DEFAULT GETDATE(),
    tipo_atividade NVARCHAR(30) NOT NULL,
    horas_gastas DECIMAL(8,2) NOT NULL,
    custo_hora DECIMAL(12,2) NOT NULL DEFAULT 0,
    valor_total_horas AS (horas_gastas * custo_hora) PERSISTED,
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_HorasPedido_Pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    CONSTRAINT CK_HorasPedido_TipoAtividade
        CHECK (tipo_atividade IN ('ARTE', 'IMPRESSAO', 'CORTE', 'MONTAGEM', 'ACABAMENTO', 'EMBALAGEM')),
    CONSTRAINT CK_HorasPedido_HorasGastas
        CHECK (horas_gastas > 0),
    CONSTRAINT CK_HorasPedido_CustoHora
        CHECK (custo_hora >= 0)
);
GO

-- =========================================
-- 11. FRETES
-- =========================================
CREATE TABLE Fretes (
    id_frete INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    tipo_frete NVARCHAR(30) NOT NULL,
    valor_frete DECIMAL(12,2) NOT NULL DEFAULT 0,
    custo_frete DECIMAL(12,2) NOT NULL DEFAULT 0,
    endereco_entrega NVARCHAR(200) NULL,
    data_envio DATETIME NULL,
    data_entrega DATETIME NULL,
    status_frete NVARCHAR(20) NOT NULL,
    codigo_rastreio NVARCHAR(100) NULL,
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_Fretes_Pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    CONSTRAINT CK_Fretes_TipoFrete
        CHECK (tipo_frete IN ('ENTREGA_PROPRIA', 'RETIRADA', 'CORREIOS', 'TRANSPORTADORA', 'MOTOBOY')),
    CONSTRAINT CK_Fretes_StatusFrete
        CHECK (status_frete IN ('PENDENTE', 'ENVIADO', 'ENTREGUE', 'CANCELADO'))
);
GO

-- =========================================
-- 12. PAGAMENTOS
-- =========================================
CREATE TABLE Pagamentos (
    id_pagamento INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    data_pagamento DATETIME NULL,
    valor_pago DECIMAL(12,2) NOT NULL,
    forma_pagamento NVARCHAR(30) NOT NULL,
    status_pagamento NVARCHAR(20) NOT NULL,
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_Pagamentos_Pedidos
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    CONSTRAINT CK_Pagamentos_ValorPago
        CHECK (valor_pago >= 0),
    CONSTRAINT CK_Pagamentos_FormaPagamento
        CHECK (forma_pagamento IN ('PIX', 'CARTAO', 'DINHEIRO', 'TRANSFERENCIA', 'BOLETO')),
    CONSTRAINT CK_Pagamentos_StatusPagamento
        CHECK (status_pagamento IN ('PENDENTE', 'PARCIAL', 'PAGO', 'ESTORNADO'))
);
GO

-- =========================================
-- 13. MOVIMENTAÇÕES DE ESTOQUE
-- =========================================
CREATE TABLE EstoqueMovimentacoes (
    id_movimentacao INT IDENTITY(1,1) PRIMARY KEY,
    id_material INT NOT NULL,
    tipo_movimentacao NVARCHAR(10) NOT NULL,
    origem_movimentacao NVARCHAR(30) NOT NULL,
    id_origem INT NULL,
    quantidade DECIMAL(18,4) NOT NULL,
    data_movimentacao DATETIME NOT NULL DEFAULT GETDATE(),
    observacoes NVARCHAR(500) NULL,
    CONSTRAINT FK_EstoqueMovimentacoes_Materiais
        FOREIGN KEY (id_material) REFERENCES Materiais(id_material),
    CONSTRAINT CK_EstoqueMovimentacoes_Tipo
        CHECK (tipo_movimentacao IN ('ENTRADA', 'SAIDA', 'AJUSTE')),
    CONSTRAINT CK_EstoqueMovimentacoes_Origem
        CHECK (origem_movimentacao IN ('COMPRA', 'CONSUMO_PEDIDO', 'PERDA', 'CORRECAO', 'DEVOLUCAO')),
    CONSTRAINT CK_EstoqueMovimentacoes_Quantidade
        CHECK (quantidade > 0)
);
GO