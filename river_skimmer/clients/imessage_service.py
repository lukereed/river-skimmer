"""
Sends a message via iMessage
"""
import os


def send_message(phone_number, message):
    """
    Sends an iMessage

    Parameters:
        phone_number (int): 10 digit phone number
        message (str): Message to send
    """
    os.system(
        f'osascript river_skimmer/clients/send_imessage.applescript {phone_number} "{message}"'
    )
