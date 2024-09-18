import redis.asyncio
import redis
import settings


def dsn(
    scheme: str,
    host: str,
    port: int,
    user: str,
    password: str,
    database: int,
):
    return f"{scheme}://{user}:{password}@{host}:{port}/{database}"


async def from_url(url: str):
    return await redis.asyncio.from_url(url)
