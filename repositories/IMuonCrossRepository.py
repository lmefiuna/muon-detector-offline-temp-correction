from abc import ABC, abstractmethod

class IMuonCrossRepository(ABC):
    @abstractmethod
    def getTMB3ByStartAndEndTimestamp(start_timestamp: int, end_timestamp: int) -> list[dict]:
        pass