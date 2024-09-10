"""Test the main module"""

import pandas as pd
import pytest

from src.main import initial_segmentation

INDEX_RANGE = range(44, 78)
INTERVENTION = 58


@pytest.mark.parametrize(
    "data, expected",
    [
        ([1] * 34, "M"),
        ([1] * 2 + [4] * 2 + [1] * 30, "X1"),
        ([1] * 19 + [5] * 15, "H"),
        ([1] * 8 + [3] * 3 + [1] * 8 + [6] * 15, "X1"),
        ([1] * 14 + [2] * 20, "H"),
        ([2] * 34, "M"),
        ([2] * 19 + [3] * 8 + [4] * 7, "X2"),
        ([2] * 16 + [1] * 18, "B"),
        ([2] * 19 + [1] * 11 + [2] * 4, "X2"),
    ],
)
def test_initial_segmentation(data, expected):
    """Test the initial_segmentation function"""
    series = pd.Series(data, index=INDEX_RANGE)
    assert initial_segmentation(series, INTERVENTION) == expected
