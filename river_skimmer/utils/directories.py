"""
Helper methods for directories
"""
import os


def make_dir_if_not_exist(path: str) -> None:
    """
    Checks if a directory exists and makes it if it does not
    """
    if not os.path.exists(path):
        os.makedirs(path)
