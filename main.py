import asyncio
from app.services.inserir import inserir
from app.services.listar import listar
from app.services.atualizar import atualizar
from app.services.incident_service import listar_incidentes
from app.utils.limpar import limpar

def pausa():
    input('Pressione Enter para continuar...')

async def main():
    while True:
        limpar()  # limpa aqui no começo do loop
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
            pausa()
        elif opcao == '2':
            await listar()
            pausa()
        elif opcao == '3':
            await atualizar()
            pausa()
        elif opcao == '4':
            print('Opção 4 ainda não implementada.')
            pausa()
        elif opcao == '5':
            print('Opção 5 ainda não implementada.')
            pausa()
        elif opcao == '6':
            print('Encerrando...')
            break
        else:
            print('Opção inválida, escolha novamente.')
            pausa()

if __name__ == '__main__':
    asyncio.run(main())
