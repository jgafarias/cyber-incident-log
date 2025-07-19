from .incident_service import listar_incidentes
from app.utils.limpar import limpar

async def listar():
    listar = await listar_incidentes()
    
    if not listar:
        print('Nenhum incidente encontrado.')
        input('Pressione Enter para voltar ao menu.')
        return

    print(f'{"ID": <3} | {"Tipo":<15} | {"Data":<10} | {"IP Origem":<15} | {"Status":<15} | Descrição')
    print('-' * 90)

    for incidente in listar:
        id_, tipo, data, ip, status, descricao = incidente
        print(f'{id_: <3} | {tipo:<15} | {str(data):<10} | {ip:<15} | {status:<15} | {descricao}')
    
    
    