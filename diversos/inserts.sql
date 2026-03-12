INSERT INTO Clientes (nome, telefone, instagram, endereco, cidade, estado, cep, observacoes)
VALUES
('testeMaria', '11911111111', 'testeMariaInsta', 'Rua Teste 1', 'CidadeTeste', 'SP', '14400000', 'cliente teste'),
('testeJoao', '11922222222', 'testeJoaoInsta', 'Rua Teste 2', 'CidadeTeste', 'SP', '14400001', 'cliente teste'),
('testeAna', '11933333333', 'testeAnaInsta', 'Rua Teste 3', 'CidadeTeste', 'SP', '14400002', 'cliente teste'),
('testeCarlos', '11944444444', 'testeCarlosInsta', 'Rua Teste 4', 'CidadeTeste', 'SP', '14400003', 'cliente teste'),
('testeJulia', '11955555555', 'testeJuliaInsta', 'Rua Teste 5', 'CidadeTeste', 'SP', '14400004', 'cliente teste'),
('testePedro', '11966666666', 'testePedroInsta', 'Rua Teste 6', 'CidadeTeste', 'SP', '14400005', 'cliente teste'),
('testeFernanda', '11977777777', 'testeFernandaInsta', 'Rua Teste 7', 'CidadeTeste', 'SP', '14400006', 'cliente teste'),
('testeBruno', '11988888888', 'testeBrunoInsta', 'Rua Teste 8', 'CidadeTeste', 'SP', '14400007', 'cliente teste'),
('testeCamila', '11999999999', 'testeCamilaInsta', 'Rua Teste 9', 'CidadeTeste', 'SP', '14400008', 'cliente teste'),
('testeLucas', '11910101010', 'testeLucasInsta', 'Rua Teste 10', 'CidadeTeste', 'SP', '14400009', 'cliente teste');
GO

INSERT INTO Produtos (nome_produto, descricao, categoria, preco_base, tipo_produto, usa_materiais, controla_estoque)
VALUES
('testeTopoBolo', 'produto teste', 'decoracao', 30, 'PERSONALIZADO', 1, 0),
('testeCaixaMilk', 'produto teste', 'lembrancinha', 12, 'PERSONALIZADO', 1, 0),
('testeConvite', 'produto teste', 'papelaria', 5, 'PERSONALIZADO', 1, 0),
('testeAdesivo', 'produto teste', 'papelaria', 2, 'PERSONALIZADO', 1, 0),
('testeTag', 'produto teste', 'papelaria', 1.5, 'PERSONALIZADO', 1, 0),
('testeCaderno', 'produto teste', 'papelaria', 40, 'PRONTA_ENTREGA', 0, 1),
('testeCaneca', 'produto teste', 'personalizados', 35, 'PRONTA_ENTREGA', 0, 1),
('testeKitFesta', 'produto teste', 'festa', 80, 'PERSONALIZADO', 1, 0),
('testePlacaDecorativa', 'produto teste', 'decoracao', 50, 'PERSONALIZADO', 1, 0),
('testePainelFesta', 'produto teste', 'decoracao', 120, 'PERSONALIZADO', 1, 0);
GO

INSERT INTO Materiais (nome_material, descricao, unidade_medida, quantidade_atual, quantidade_minima, custo_medio, local_armazenamento)
VALUES
('testePapelFotografico', 'material teste', 'folha', 200, 50, 1.20, 'prateleiraA'),
('testePapelOffset', 'material teste', 'folha', 300, 80, 0.80, 'prateleiraA'),
('testePapelColorido', 'material teste', 'folha', 150, 40, 0.90, 'prateleiraB'),
('testeAcetato', 'material teste', 'folha', 100, 20, 2.50, 'prateleiraB'),
('testeFitaCetim', 'material teste', 'metro', 500, 100, 0.30, 'gaveta1'),
('testeCola', 'material teste', 'unidade', 80, 20, 5.00, 'gaveta2'),
('testeTintaImpressora', 'material teste', 'cartucho', 20, 5, 45.00, 'armario1'),
('testePalitoTopper', 'material teste', 'unidade', 500, 100, 0.05, 'caixa1'),
('testeLaminacao', 'material teste', 'folha', 200, 50, 1.50, 'prateleiraC'),
('testeEmbalagem', 'material teste', 'unidade', 300, 60, 0.70, 'caixa2');
GO

INSERT INTO Fornecedores (razao_nome, nome_fantasia, cpf_cnpj, telefone, email, endereco, cidade, estado, cep, contato_responsavel)
VALUES
('testeFornecedor1', 'testePapelariaA', '00000000000101', '1131111111', 'teste1@email.com', 'Rua Teste 11', 'CidadeTeste', 'SP', '14400010', 'testeCarlos'),
('testeFornecedor2', 'testePapelariaB', '00000000000102', '1132222222', 'teste2@email.com', 'Rua Teste 12', 'CidadeTeste', 'SP', '14400011', 'testeMaria'),
('testeFornecedor3', 'testePapelariaC', '00000000000103', '1133333333', 'teste3@email.com', 'Rua Teste 13', 'CidadeTeste', 'SP', '14400012', 'testeJoao'),
('testeFornecedor4', 'testePapelariaD', '00000000000104', '1134444444', 'teste4@email.com', 'Rua Teste 14', 'CidadeTeste', 'SP', '14400013', 'testeAna'),
('testeFornecedor5', 'testePapelariaE', '00000000000105', '1135555555', 'teste5@email.com', 'Rua Teste 15', 'CidadeTeste', 'SP', '14400014', 'testePedro'),
('testeFornecedor6', 'testePapelariaF', '00000000000106', '1136666666', 'teste6@email.com', 'Rua Teste 16', 'CidadeTeste', 'SP', '14400015', 'testeJulia'),
('testeFornecedor7', 'testePapelariaG', '00000000000107', '1137777777', 'teste7@email.com', 'Rua Teste 17', 'CidadeTeste', 'SP', '14400016', 'testeLucas'),
('testeFornecedor8', 'testePapelariaH', '00000000000108', '1138888888', 'teste8@email.com', 'Rua Teste 18', 'CidadeTeste', 'SP', '14400017', 'testeBruno'),
('testeFornecedor9', 'testePapelariaI', '00000000000109', '1139999999', 'teste9@email.com', 'Rua Teste 19', 'CidadeTeste', 'SP', '14400018', 'testeFernanda'),
('testeFornecedor10', 'testePapelariaJ', '00000000000110', '1130000000', 'teste10@email.com', 'Rua Teste 20', 'CidadeTeste', 'SP', '14400019', 'testeCamila');
GO

INSERT INTO Compras (id_fornecedor, data_compra, data_recebimento, valor_total, status_compra, observacoes)
VALUES
(1, GETDATE(), GETDATE(), 500, 'RECEBIDA', 'testeCompra1'),
(2, GETDATE(), GETDATE(), 350, 'RECEBIDA', 'testeCompra2'),
(3, GETDATE(), GETDATE(), 600, 'RECEBIDA', 'testeCompra3'),
(4, GETDATE(), GETDATE(), 200, 'RECEBIDA', 'testeCompra4'),
(5, GETDATE(), GETDATE(), 420, 'RECEBIDA', 'testeCompra5'),
(6, GETDATE(), GETDATE(), 310, 'RECEBIDA', 'testeCompra6'),
(7, GETDATE(), GETDATE(), 280, 'RECEBIDA', 'testeCompra7'),
(8, GETDATE(), GETDATE(), 450, 'RECEBIDA', 'testeCompra8'),
(9, GETDATE(), GETDATE(), 390, 'RECEBIDA', 'testeCompra9'),
(10, GETDATE(), GETDATE(), 520, 'RECEBIDA', 'testeCompra10');
GO

INSERT INTO ItensCompra (id_compra, id_material, quantidade, valor_unitario)
VALUES
(1,1,100,1.20),
(2,2,150,0.80),
(3,3,120,0.90),
(4,4,80,2.50),
(5,5,200,0.30),
(6,6,40,5.00),
(7,7,10,45.00),
(8,8,300,0.05),
(9,9,150,1.50),
(10,10,200,0.70);
GO

INSERT INTO Pedidos (id_cliente, data_pedido, data_entrega_prevista, status_pedido, tema_personalizacao, descricao_personalizacao, valor_produtos, valor_mao_obra, valor_frete, valor_desconto, valor_total, observacoes)
VALUES
(1,GETDATE(),GETDATE(),'APROVADO','testeTema1','testePedido1',120,30,15,0,165,'testePedido'),
(2,GETDATE(),GETDATE(),'APROVADO','testeTema2','testePedido2',80,20,10,0,110,'testePedido'),
(3,GETDATE(),GETDATE(),'APROVADO','testeTema3','testePedido3',150,40,20,0,210,'testePedido'),
(4,GETDATE(),GETDATE(),'APROVADO','testeTema4','testePedido4',60,15,10,0,85,'testePedido'),
(5,GETDATE(),GETDATE(),'APROVADO','testeTema5','testePedido5',200,50,25,0,275,'testePedido'),
(6,GETDATE(),GETDATE(),'APROVADO','testeTema6','testePedido6',90,25,15,0,130,'testePedido'),
(7,GETDATE(),GETDATE(),'APROVADO','testeTema7','testePedido7',130,35,20,0,185,'testePedido'),
(8,GETDATE(),GETDATE(),'APROVADO','testeTema8','testePedido8',75,18,12,0,105,'testePedido'),
(9,GETDATE(),GETDATE(),'APROVADO','testeTema9','testePedido9',160,45,18,0,223,'testePedido'),
(10,GETDATE(),GETDATE(),'APROVADO','testeTema10','testePedido10',110,30,15,0,155,'testePedido');
GO

INSERT INTO ItensPedido (id_pedido, id_produto, descricao_item_personalizado, quantidade, valor_unitario)
VALUES
(1,1,'testeItem1',2,30),
(2,2,'testeItem2',10,5),
(3,3,'testeItem3',20,2),
(4,4,'testeItem4',15,3),
(5,5,'testeItem5',25,4),
(6,6,'testeItem6',1,40),
(7,7,'testeItem7',2,35),
(8,8,'testeItem8',5,10),
(9,9,'testeItem9',3,50),
(10,10,'testeItem10',1,120);
GO

INSERT INTO ConsumoMateriaisPedido (id_pedido, id_item_pedido, id_material, quantidade_consumida, custo_unitario_material, observacoes)
VALUES
(1,1,1,5,1.20,'testeConsumo'),
(2,2,2,10,0.80,'testeConsumo'),
(3,3,3,8,0.90,'testeConsumo'),
(4,4,4,6,2.50,'testeConsumo'),
(5,5,5,20,0.30,'testeConsumo'),
(6,6,6,2,5.00,'testeConsumo'),
(7,7,7,1,45.00,'testeConsumo'),
(8,8,8,15,0.05,'testeConsumo'),
(9,9,9,4,1.50,'testeConsumo'),
(10,10,10,6,0.70,'testeConsumo');
GO  

INSERT INTO HorasPedido (id_pedido, tipo_atividade, horas_gastas, custo_hora, observacoes)
VALUES
(1,'ARTE',1.5,25,'testeHora'),
(2,'IMPRESSAO',1.0,25,'testeHora'),
(3,'CORTE',2.0,25,'testeHora'),
(4,'MONTAGEM',1.2,25,'testeHora'),
(5,'ACABAMENTO',1.8,25,'testeHora'),
(6,'EMBALAGEM',0.8,25,'testeHora'),
(7,'ARTE',1.3,25,'testeHora'),
(8,'IMPRESSAO',1.1,25,'testeHora'),
(9,'CORTE',2.2,25,'testeHora'),
(10,'MONTAGEM',1.4,25,'testeHora');
GO

INSERT INTO Fretes (id_pedido, tipo_frete, valor_frete, custo_frete, endereco_entrega, status_frete, observacoes)
VALUES
(1,'MOTOBOY',15,10,'Endereco teste 1','ENVIADO','testeFrete'),
(2,'RETIRADA',0,0,'Endereco teste 2','ENTREGUE','testeFrete'),
(3,'CORREIOS',20,15,'Endereco teste 3','ENVIADO','testeFrete'),
(4,'MOTOBOY',10,8,'Endereco teste 4','ENTREGUE','testeFrete'),
(5,'CORREIOS',25,20,'Endereco teste 5','ENVIADO','testeFrete'),
(6,'RETIRADA',0,0,'Endereco teste 6','ENTREGUE','testeFrete'),
(7,'TRANSPORTADORA',30,22,'Endereco teste 7','ENVIADO','testeFrete'),
(8,'MOTOBOY',12,9,'Endereco teste 8','ENTREGUE','testeFrete'),
(9,'CORREIOS',18,14,'Endereco teste 9','ENVIADO','testeFrete'),
(10,'MOTOBOY',15,11,'Endereco teste 10','ENTREGUE','testeFrete');
GO

INSERT INTO Pagamentos (id_pedido, data_pagamento, valor_pago, forma_pagamento, status_pagamento, observacoes)
VALUES
(1,GETDATE(),165,'PIX','PAGO','testePagamento'),
(2,GETDATE(),110,'DINHEIRO','PAGO','testePagamento'),
(3,GETDATE(),210,'CARTAO','PAGO','testePagamento'),
(4,GETDATE(),85,'PIX','PAGO','testePagamento'),
(5,GETDATE(),275,'TRANSFERENCIA','PAGO','testePagamento'),
(6,GETDATE(),130,'PIX','PAGO','testePagamento'),
(7,GETDATE(),185,'CARTAO','PAGO','testePagamento'),
(8,GETDATE(),105,'DINHEIRO','PAGO','testePagamento'),
(9,GETDATE(),223,'PIX','PAGO','testePagamento'),
(10,GETDATE(),155,'TRANSFERENCIA','PAGO','testePagamento');
GO

