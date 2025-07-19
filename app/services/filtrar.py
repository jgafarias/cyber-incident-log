from .incident_service import filtrar_incidentes
from ..utils.limpar import limpar

async def filtrar():
    status_opcoes = {
        '1': 'Em análise',
        '2': 'Análise completa',
        '3': 'Aguardando resposta',
        '4': 'Resolvido',
        '5': 'Fechado',
        '6': 'Reaberto',
        '7': 'Ignorado',        
    }

    limpar()
    print("\nEscolha o status para ser exibido:")
    for chave, valor in status_opcoes.items():
        print(f"{chave}. {valor}")
        
    opcao = input('Digite o número do status: ').strip()
    status = status_opcoes.get(opcao)

    if not status:
        print("Opção inválida.")
        input('Pressione Enter para voltar ao menu.')
        return

    incidentes = await filtrar_incidentes(status)

    if not incidentes:
        print('Nenhum incidente com esse status foi encontrado.')
        input('Pressione Enter para voltar ao menu.')
        return

    print(f'\n{"ID": <3} | {"Tipo":<15} | {"Data":<10} | {"IP Origem":<15} | {"Status":<15} | Descrição')
    print('-' * 90)

    for incidente in incidentes:
        id_, tipo, data, ip_origem, status, descricao = incidente
        print(f'{id_: <3} | {tipo:<15} | {str(data):<10} | {ip_origem:<15} | {status:<15} | {descricao}')

    print()
    input('Pressione Enter para voltar ao menu.')
