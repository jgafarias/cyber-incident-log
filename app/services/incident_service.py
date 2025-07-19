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

            return resultados
    except Exception as e:
        print(f'Erro ao listar os incidentes: {e}')
        return []
    finally:
        await con.ensure_closed()
        
async def atualizar_incidente(id_incidente, novo_status):
    con = await connection()
    try: 
        async with con.cursor() as c:
            # Verifica se o incidente existe
            await c.execute('SELECT id FROM incidentes WHERE id = %s', (id_incidente,))
            resultado = await c.fetchone()
            
            if not resultado:
                print(f'Incidente com ID {id_incidente} não encontrado.')
                return

            # Atualiza o status
            sql = 'UPDATE incidentes SET status = %s WHERE id = %s'
            await c.execute(sql, (novo_status, id_incidente))
            await con.commit()
            print('Incidente atualizado com sucesso!')
    except Exception as e:
        print(f'Erro ao atualizar o incidente: {e}')
    finally:
        await con.ensure_closed()
