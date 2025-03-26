"""
A script to monitor a target campsite on Ruby Horsethief
"""
import datetime
from time import sleep

from river_skimmer.rivers.permit import Permit
from river_skimmer.campsites.ruby_horsethief import RubyHorsethief
from river_skimmer.clients.recreation_service import get_camp_details
from river_skimmer.clients.imessage_service import send_message


class RubyMonitor:
    """
    Monitors Ruby Horsethief campsite(s) to see when it becomes available

    Parameters:
        date (datetime.date): Date of interest
        campsite (str): Campsite to monitor
    """
    def __init__(
        self,
        date: datetime.date,
        campsite: RubyHorsethief,
        phone_number: int,
        timeout: datetime.timedelta = datetime.timedelta(hours=8),
    ):
        self.date = date
        self.campsite = campsite
        self.phone_number = phone_number
        self.timeout = timeout

        self.start_time: datetime.datetime = None
        self.total: int = None
        self.remaining: int = None

    def scan(self) -> None:
        """
        Continually scans the campsite status until it becomes available or
        the timeout is hit.
        """
        self.start_time = datetime.datetime.now()
        print(f"Start Time: {self.start_time.now().strftime('%Y-%m-%d %H:%M:%S')}")
        while datetime.datetime.now() < self.start_time + self.timeout:
            try:
                self._scan()
                if self.remaining > 0:
                    message = f"""{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {self.remaining} available at {self.campsite.name}
https://www.recreation.gov/permits/{Permit.RubyHorsethief.id}/registration/detailed-availability?date={self.date.strftime("%Y-%m-%d")}"""
                    print(message)
                    send_message(
                        phone_number=self.phone_number,
                        message=message,
                    )
                    break
                sleep(1)
            except IndexError:
                pass

    def _scan(self):
        availability = get_camp_details(
            section=Permit.RubyHorsethief,
            month=self.date.month,
            year=self.date.year,
        )
        site_data = availability[str(self.campsite.id)]['date_availability']
        status = [{k: v} for k, v in site_data.items() if k == self.date_string][0][self.date_string]
        self.total = status['total']
        self.remaining = status['remaining']

    @property
    def date_string(self) -> str:
        """
        Returns the object date in datetime string format of Recreation.gov
        """
        return self.date.strftime('%Y-%m-%dT00:00:00Z')


if __name__ == "__main__":
    ruby_monitor = RubyMonitor(
        date=datetime.date(
            year=2025,
            month=5,
            day=14,
        ),
        campsite=RubyHorsethief.Rattlesnake,
        phone_number=1234567891,
    )
    ruby_monitor.scan()
