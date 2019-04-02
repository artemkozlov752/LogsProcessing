import os
import pandas as pd
import pytest

from parsers.LogProcessing import LogProcessing
from util import get_config


PATH_TO_CONFIG_FOR_TESTS = os.path.join(".", "tests", "configs", "config.yaml")
CONFIG_FOR_TESTS = get_config(PATH_TO_CONFIG_FOR_TESTS)


@pytest.fixture
def test_files_zip():
    return os.path.join(".", "tests", "test_logs.zip")


@pytest.fixture
def correct_dataframe():
    columns = CONFIG_FOR_TESTS["dataframe"]
    dataframe = pd.DataFrame(columns).set_index('timestamp')
    return dataframe


def test_download_logs(test_files_zip, correct_dataframe):
    log_processor = LogProcessing(test_files_zip)
    dataframe = log_processor.read_zip_file().set_index('timestamp')
    for index in correct_dataframe.index:
        for column in correct_dataframe.columns:
            assert_message = f"Incorrect result for index={index}, column={column}"
            assert correct_dataframe.loc[index][column] == dataframe.loc[index][column], assert_message
