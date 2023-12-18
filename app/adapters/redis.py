import redis.asyncio
from redis.asyncio import Redis as _Redis


class Redis(_Redis):
    ...


def dsn(
    scheme: str,
    host: str,
    port: int,
    user: str,
    password: str,
    database: int,
):
    return f"{scheme}://{user}:{password}@{host}:{port}/{database}"


async def from_url(url: str) -> Redis:
    return await redis.asyncio.from_url(url)
