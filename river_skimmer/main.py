"""
Determines permit availability for all rivers specified in Permit.river_sections
"""
from datetime import datetime as dt
import pandas as pd

from river_skimmer.rivers.permit import Permit
from river_skimmer.clients.recreation_service import get_river_availability


class RiverPermitFinder:
    """
    Finds a recreation.gov permit
    """

    def __init__(self, start_date: dt, end_date: dt):
        # TODO: If no dates are supplies, use lottery window
        self.start_date = start_date
        self.end_date = end_date

        self.availability: pd.Series = None
        self.df: pd.DataFrame = None

    def run(self) -> None:
        """
        Determines permit availability for all rivers
        """
        self.df: pd.DataFrame = pd.DataFrame(
            index=pd.date_range(
                start=self.start_date,
                end=self.end_date,
                freq='1d',
            ),
        )

        for section in Permit().river_sections:
            availability = get_river_availability(
                section=section,
                start_date=self.start_date,
                end_date=self.end_date,
            )
            self.df[availability.name] = availability

        self.df.dropna(
            axis=0,
            how='all',
            inplace=True,
        )
