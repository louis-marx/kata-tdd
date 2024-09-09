""" Main module for the store segmentation project """

import pandas as pd


def initial_segmentation(weekly_store_typo: pd.Series, intervention: int) -> str:
    """
    Segment the store based on the store typology history

    Args:
        series (pd.Series): Store typology over weeks

    Returns:
        str: Store initial class
    """
    return ""
