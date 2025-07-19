from app.db.config import connection
import asyncio

async def inserir_incidente(tipo, data_ocorrencia, ip_origem, status, descricao):
    con = await connection()
    try:
        async with con.cursor() as c:
            sql = '''INSERT INTO incidentes(tipo, data_ocorrencia, ip_origem, status, descricao) VALUES (%s, %s, %s, %s, %s)'''
            await c.execute(sql, (tipo, data_ocorrencia, ip_origem, status, descricao))
            await con.commit()
        print('Incidente cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar incidente: {e}')
    finally:
        await con.ensure_closed()
        
async def listar_incidentes():
    con = await connection()
    try:
        async with con.cursor() as c:
            sql = 'SELECT * FROM incidentes'
            await c.execute(sql)
            resultados = await c.fetchall()
            
            if not resultados:
                print('Nenhum incidente encontrado.')
                return
            
            print(f'{'ID': <3} | {'Tipo':<15} | {'Data':<10} | {'IP Origem':<15} | {'Status':<10} | Descrição')
            print('-' * 80)
            
            for incidente in resultados:
                id_, tipo, data, ip, status, descricao = incidente
                print(f'{id_: <3} | {tipo:<15} | {str(data):<10} | {ip:<15} | {status:<10} | {descricao}')
            
    except Exception as e:
        print(f'Erro ao listar os incidentes: {e}')
    finally:
        await con.ensure_closed()