import os
import pandas as pd
import pytest

from parsers.LogProcessing import create_is_valid_field
from util import get_config


PATH_TO_CONFIG_FOR_TESTS = os.path.join(".", "tests", "configs", "config.yaml")
CONFIG_FOR_TESTS = get_config(PATH_TO_CONFIG_FOR_TESTS)


@pytest.fixture
def dataframe():
    columns = CONFIG_FOR_TESTS["dataframe"]
    dataframe = pd.DataFrame(columns)
    return dataframe


@pytest.fixture
def correct_is_valid_column():
    is_valid = CONFIG_FOR_TESTS["is_valid_column"]
    return is_valid


@pytest.fixture
def grouped_dataframe():
    columns = CONFIG_FOR_TESTS["correct_grouped_dataframe"]
    dataframe = pd.DataFrame(columns).set_index(["is_valid", "timestamp", "event_type"])
    return dataframe


def test_is_valid_function(dataframe, correct_is_valid_column):
    dataframe['is_valid'] = dataframe.apply(create_is_valid_field, axis=1)
    for element, correct_element in zip(dataframe['is_valid'], correct_is_valid_column):
        assert_message = "Incorrect result, check your function for creating is_valid column"
        assert element == correct_element, assert_message
