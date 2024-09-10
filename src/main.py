"""Main module for the TDD kata"""

import pandas as pd


def initial_segmentation(weekly_store_typo: pd.Series, intervention: int) -> str:
    """
    Segment the store based on the store typology history

    Args:
        series (pd.Series): Store typology over weeks

    Returns:
        str: Store initial class
    """
    if weekly_store_typo.diff().nunique() == 1:
        return "M"
    if weekly_store_typo[weekly_store_typo.index < intervention].nunique() > 1:
        return "X1"
    if weekly_store_typo.diff().ne(0).sum() == 2:
        pre, post = weekly_store_typo.unique()
        return "B" if pre > post else "H"
    return "X2"
