"""
Sends a message via SMS
"""
import smtplib
from dataclasses import dataclass

from river_skimmer.clients.config import (
    SMTP_EMAIL_ADDRESS,
    SMTP_PASSWORD,
    SMTP_SERVER,
)


@dataclass
class Domain:
    """
    Describes a phone service provider domain for email to SMS
    """
    name: str
    domain: str


@dataclass
class Carrier:
    """
    Library of Phone Carrier Domains
    """
    ATT = Domain(
        name="att",
        domain="@txt.att.net",
    )


def send_message(phone_number: int, message: str) -> None:
    """
    Sends a text message from an email account

    Parameters:
        phone_number (str): 10 digit phone number without spaces followed by carrier domain
        carrier (Carrier): Phone Carrier
        message (str): Message to send
    """

    server = smtplib.SMTP(SMTP_SERVER, 587)
    server.starttls()
    server.login(
        user=SMTP_EMAIL_ADDRESS,
        password=SMTP_PASSWORD,
    )

    server.sendmail(
        from_addr=SMTP_EMAIL_ADDRESS,
        to_addrs=phone_number,
        msg=message,
    )
