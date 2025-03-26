"""
Example usage to extract Ruby Horsethief campsite availability
"""
import pandas as pd

from river_skimmer.rivers.permit import Permit
from river_skimmer.campsites.ruby_horsethief import RubyHorsethief
from river_skimmer.clients.recreation_service import get_camp_details
from river_skimmer.utils.directories import make_dir_if_not_exist


class RubyCampsites:
    """
    Compiles availability of Ruby Horsethief Campsites for specified
    year and month

    Parameters:
        month (int): Month of interest
        year (int): Year of interest
    """

    def __init__(self, month: int, year: int):
        self.month = month
        self.year = year

        self.df: pd.DataFrame() = pd.DataFrame()

        self._build()

    def _build(self) -> None:
        availability = get_camp_details(
            section=Permit.RubyHorsethief,
            month=self.month,
            year=self.year,
        )
        for camp in RubyHorsethief().camps:
            dates = availability[str(camp.id)]['date_availability']
            for date, data in dates.items():
                col = date[5:10]
                self.df.loc[camp.name, col] = int(data['remaining'])


if __name__ == "__main__":
    camps = RubyCampsites(
        month=5,
        year=2025,
    )
    make_dir_if_not_exist('output')
    make_dir_if_not_exist(f'output/{camps.year}')
    camps.df.to_csv(
        f'output/{camps.year}/RubyCampsites-{camps.year}-{camps.month}.csv')
