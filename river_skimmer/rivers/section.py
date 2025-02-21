"""
Data structure for a river section
"""
from dataclasses import dataclass


@dataclass
class Section:
    """
    Describes a river section

    Parameters:
        id (int): Recreation.gov API identifier
        entrance (int): Recreation.gov launch point identifier
        name (str): Name of river section
        river (str): Name of river
        put_in (str): Name of Put-In
        take_out (str): Name of Take-Out
    """
    id: int
    entrance: int
    name: str
    river: str
    put_in: str
    take_out: str
    # TODO: Add Lottery Start and End Dates
