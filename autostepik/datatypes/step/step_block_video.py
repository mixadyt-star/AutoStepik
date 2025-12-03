from dataclasses import dataclass
from typing import List
from .block_video_url import StepBlockVideoUrl


@dataclass
class StepBlockVideo:
    id: int
    thumbnail: str
    urls: List[StepBlockVideoUrl]
    duration: int
    status: str
    upload_date: str
    filename: str