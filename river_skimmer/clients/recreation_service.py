"""
Client to interact with Recreation.gov `/availability` endpoint
"""
from collections import ChainMap
import random
import requests
import pandas as pd

from river_skimmer.rivers.permit import Section
from river_skimmer.clients.config import RECREATION_API_BASE_URL


USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]


def get_river_availability(section: Section, start_date: str, end_date: str) -> pd.Series:
    """
    Creates a request for status of a particular river section

    Parameters:
        section (Section): River section of interest
        start_date (str): Start date in the format YYYY-mm-dd
        end_date (str): end date in the format YYYY-mm-dd

    Returns:
        pd.Series: Series of available launch dates
    """
    session = requests.Session()
    river_availability = session.get(
        url=f'{RECREATION_API_BASE_URL}permits/{section.id}/divisions/{section.entrance}/availability',
        headers={'User-Agent': random.choice(USER_AGENTS)},
        params={
            "start_date": f'{start_date}T00:00:00.000Z',
            "end_date": f'{end_date}T00:00:00.000Z',
            "commercial_acc": False,
            "is_lottery": False,
        }
    )
    river_availability.raise_for_status()
    availability = river_availability.json()['payload']['date_availability']
    available_dates = [
        {key.split('T')[0]: val['remaining']} for key, val in availability.items() if val['remaining'] > 0
    ]
    available_dates = pd.Series(
        dict(ChainMap(*available_dates)),
        name=section.name,
    )
    available_dates.index = pd.to_datetime(available_dates.index)

    return available_dates


def get_camp_details(section: Section, month: int, year: int) -> dict:
    """
    Retrieves available camp site details

    Parameters:
        section (Section): River section of interest
        month (int): Month of interest
        year (int): Year of interest

    Returns:
        dict: Dictionary of camp availability
    """
    session = requests.Session()
    camp_details = session.get(
        url=f'{RECREATION_API_BASE_URL}permits/{section.id}/availability/month',
        headers={'User-Agent': random.choice(USER_AGENTS)},
        params={
            "start_date": f'{year}-{str(month).zfill(2)}-01T00:00:00.000Z',
        }
    )
    camp_details.raise_for_status()
    details = camp_details.json()['payload']['availability']
    return details
