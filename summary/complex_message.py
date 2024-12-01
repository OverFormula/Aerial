from dataclasses import dataclass
from typing import Any


@dataclass
class ComplexMessage:
  image: Any
  caption: str
