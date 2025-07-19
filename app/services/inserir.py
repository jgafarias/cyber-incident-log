from .incident_service import inserir_incidente

async def inserir():
    tipo = input('Tipo de incidente: ')
    data = input('Data do incidente (YYYY-MM-DD): ')
    ip = input('IP de origem: ')
    status = input('Status: ')
    desc = input('Descrição do incidente: ')
    
    await inserir_incidente(tipo, data, ip, status, desc)
    print('Incidente cadastrado: ')
    print(f'Tipo do incidente: {tipo}')
    print(f'Data do incidente: {data}')
    print(f'IP de origem: {ip}')
    print(f'Status: {status}')
    print(f'Descrição do incidente: {desc}')
    