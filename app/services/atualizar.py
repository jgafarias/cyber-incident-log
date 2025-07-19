from app.utils.limpar import limpar
from app.services.listar import listar_incidentes
from app.services.incident_service import atualizar_incidente

async def atualizar():
    incidentes = await listar_incidentes()

    if not incidentes:
        print('Nenhum incidente encontrado.')
        input('Pressione Enter para voltar ao menu.')
        return

    print(f'{"ID": <3} | {"Tipo":<15} | {"Data":<10} | {"IP Origem":<15} | {"Status":<15} | Descrição')
    print('-' * 90)

    for incidente in incidentes:
        id_, tipo, data, ip, status, descricao = incidente
        print(f'{id_: <3} | {tipo:<15} | {str(data):<10} | {ip:<15} | {status:<15} | {descricao}')

    try:
        id_str = input('\nDigite o ID do incidente que deseja atualizar: ').strip()
        id_incidente = int(id_str)
    except ValueError:
        print('ID inválido. Use um número inteiro.')
        input('Pressione Enter para voltar ao menu.')
        return

    # Verifica se o ID existe
    incidente_selecionado = None
    for i in incidentes:
        if i[0] == id_incidente:
            incidente_selecionado = i
            break

    if not incidente_selecionado:
        print(f'Incidente com ID {id_incidente} não encontrado.')
        input('Pressione Enter para voltar ao menu.')
        return

    limpar()

    print(f'Incidente selecionado:\nID: {incidente_selecionado[0]} | Tipo: {incidente_selecionado[1]} | Status atual: {incidente_selecionado[4]}')

    status_dict = {
        '1': 'Em análise',
        '2': 'Análise completa',
        '3': 'Aguardando resposta',
        '4': 'Resolvido',
        '5': 'Fechado',
        '6': 'Reaberto',
        '7': 'Ignorado',
    }

    print("\nEscolha o novo status:")
    for chave, valor in status_dict.items():
        print(f"{chave}. {valor}")

    opcao = input("Digite a opção do novo status: ").strip()
    novo_status = status_dict.get(opcao)

    if not novo_status:
        print("Opção inválida.")
        input("Pressione Enter para voltar ao menu.")
        return

    await atualizar_incidente(id_incidente, novo_status)
    input("Pressione Enter para voltar ao menu.")
