from enum import Enum

class NewsState(str, Enum):
    PROCESSED = "PROCESSED"
    NEED_PROCESSING = "NEED_PROCESSING"
