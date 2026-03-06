"""
Example usage to write out DataFrame of all available river permits for a 
specified time window
"""
import os

from river_skimmer.main import RiverPermitFinder
from river_skimmer.utils.directories import make_dir_if_not_exist


if __name__ == "__main__":
    permits = RiverPermitFinder(
        start_date='2026-05-12',
        end_date='2026-10-12',
        river_sections="desolation_gray",
        # river_sections="dinosaur",
        # river_sections="san_juan_salmon",
    )

    permits.run()

    make_dir_if_not_exist('output')
    permits.df.to_csv(
        os.path.join(
            'output',
            f'{permits.river_sections}_availability_{permits.start_date}_{permits.end_date}.csv',
        ),
    )
