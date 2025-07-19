import aiomysql
import os
from dotenv import load_dotenv

load_dotenv()

async def connection():
    return await aiomysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        autocommit=True
    )