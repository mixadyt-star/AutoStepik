from dataclasses import dataclass
from typing import Dict, Any, List
from .step_block_video import StepBlockVideo


@dataclass
class StepBlock:
    name: str
    text: str
    video: StepBlockVideo | None
    options: Dict[Any, Any]
    subtitle_files: List[Any]
    is_deprecated: bool