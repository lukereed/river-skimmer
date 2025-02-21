from river_skimmer.clients.recreation_service import get_river_availability
from river_skimmer.rivers.permit import Permit


if __name__ == "__main__":
    available_dates = get_river_availability(
        section=Permit.SanJuanMexicanHatClayHills,
        start_date='2025-03-15',
        end_date='2025-11-30',
    )
    print(available_dates)
