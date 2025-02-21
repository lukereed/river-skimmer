import pandas as pd

from river_skimmer.rivers.permit import Permit
from river_skimmer.campsites.ruby_horsethief import RubyHorsethief
from river_skimmer.clients.recreation_service import get_camp_details
from river_skimmer.utils.utils import make_dir_if_not_exist


class RubyCampsites:
    def __init__(self, month: int, year: int):
        self.month = month
        self.year = year

        self.df: pd.DataFrame() = pd.DataFrame()

        self.build()

    def build(self) -> None:
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
    camp_availability = RubyCampsites(
        month=4,
        year=2025,
    )
    make_dir_if_not_exist('output')
    camp_availability.df.to_csv(
        f'output/RubyCampsites-{camp_availability.year}-{camp_availability.month}.csv')
