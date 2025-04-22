from dataclasses import dataclass
from typing import List

@dataclass
class TripData:
    origin: str
    cities: List[str]
    date_range: str
    interests: List[str]
