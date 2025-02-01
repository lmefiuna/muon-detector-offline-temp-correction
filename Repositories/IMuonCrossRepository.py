from abc import ABC, abstractmethod

class IMuonCrossRepository:
    @abstractmethod
    def getTMB3ByStartAndEndTimestamp(start_timestamp: int, end_timestamp: int) -> None:
        pass