"""
Helper methods for dates
"""
from datetime import datetime


def date_string_to_dt(date: str) -> datetime:
    """
    Expects a date in m/d/yyyy form
    """
    month, day, year = date.split('/')
    return datetime(year=int(year), month=int(month), day=int(day))


def dt_to_date_string(dt: datetime) -> str:
    """
    Returns a formated date string in m/d/yyy form
    """
    return dt.strftime('%m/%d/%Y')


def dt_to_data_string(dt: datetime) -> str:
    """
    Returns a formatted datetime string for post request
    """
    return dt.strftime('%a %b %d %Y')
