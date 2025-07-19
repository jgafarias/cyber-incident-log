import asyncio
from app.services.inserir import inserir
from app.services.incident_service import listar_incidentes

async def main():
    while True:
        print('Escolha o que deseja:')
        print('1. Inserir incidente')
        print('2. Listar todos')
        print('3. Atualizar incidente')
        print('4. Filtrar por tipo/status')
        print('5. Exportar CSV')
        print('6. Sair')
        
        opcao = input('Escolha uma opção: ').strip()
        
        if opcao == '1':
            await inserir()
        if opcao == '2':
            await listar_incidentes()
        elif opcao == '6':
            print('Encerrando...')
            break
        else: 
            print('Opção inválida, escolha novamente')
        
if __name__ == '__main__':
    asyncio.run(main())