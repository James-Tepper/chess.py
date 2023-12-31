from enum import IntEnum

"""
Classical 1-2 hours
Rapid 15-30 minutes
Blitz 5-10 minutes
"""

class GameType(IntEnum):
    CLASSICAL = 3600 | 7200
    RAPID = 900 | 1800
    BLITZ = 300 | 600


