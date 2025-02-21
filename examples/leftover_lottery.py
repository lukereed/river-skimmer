import os

from river_skimmer.main import RiverPermitFinder
from river_skimmer.utils.utils import make_dir_if_not_exist


if __name__ == "__main__":
    permits = RiverPermitFinder(
        start_date='2025-05-01',
        end_date='2025-08-30',
    )
    permits.run()

    make_dir_if_not_exist('output')
    permits.df.to_csv(
        os.path.join(
            'output',
            f'RiverAvailability_{permits.start_date}_{permits.end_date}.csv',
        ),
    )
