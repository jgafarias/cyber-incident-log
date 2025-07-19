import asyncio
from ..services.incident_service import inserir_incidente

async def inserir_teste():
    await inserir_incidente(
        tipo="DoS",
        data_ocorrencia="2025-07-19",
        ip_origem="192.168.0.100",
        status="Em análise",
        descricao="Teste de inserção do incidente DoS."
    )

asyncio.run(inserir_teste())
