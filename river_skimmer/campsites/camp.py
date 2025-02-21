"""
Dataclass for camps on a given river section
"""
from dataclasses import dataclass


@dataclass
class Camp:
    """
    Describes a river section
    """
    id: int
    name: str
