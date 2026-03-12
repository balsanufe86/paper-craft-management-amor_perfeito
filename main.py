from app.services import estoque_service

movs = estoque_service.listar_movimentacoes()

for m in movs:
    print(m)