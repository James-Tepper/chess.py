from typing import Any


def info(message: str, **extra: Any):
    print(message)
    print(f"{str(k).upper()}:{v}" for k, v in extra.items())
