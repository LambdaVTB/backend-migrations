from enum import Enum

class NewsTypes(str, Enum):
    DIGEST = "DIGEST"
    INSIGHT = "INSIGHT"
    TREND = "TREND"
