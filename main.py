import asyncio
from app.services.inserir import inserir
from app.services.listar import listar
from app.services.filtrar import filtrar
from app.services.atualizar import atualizar
from app.services.incident_service import listar_incidentes
from app.utils.limpar import limpar
from app.utils.export import exportar

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
            await filtrar()
            pausa()
        elif opcao == '5':
            await exportar()
            pausa()
        elif opcao == '6':
            print('Encerrando...')
            break
        else:
            print('Opção inválida, escolha novamente.')
            pausa()

if __name__ == '__main__':
    asyncio.run(main())
