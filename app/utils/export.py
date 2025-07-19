from app.services.listar import listar_incidentes
import pandas as pd

async def exportar():
    incidentes = await listar_incidentes()
    if not incidentes:
        print("Nenhum incidente para exportar.")
        return
    
    df = pd.DataFrame(incidentes, columns=['ID', 'Tipo', 'Data', 'IP Origem', 'Status', 'Descrição'])
    try:
        df.to_csv('incidentes.csv', index=False, encoding='utf-8-sig')
        print("Arquivo 'incidentes.csv' exportado com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar o arquivo: {e}")
