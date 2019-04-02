from zipfile import ZipFile
import logging
import os
import pandas as pd
import re


def create_is_valid_field(log):
    """Check if log is valid.

    Log is valid if 'query_string' contains exactly the same set of id as in the array 'ids'

    Args:
        log (pandas.core.series.Series).

    Returns:
        "valid" if string valid; "non_valid" otherwise.

    """
    ids = sorted(log['ids'])
    query_ids = re.findall(r"id=(\d+)", log['query_string'])
    query_int_ids = sorted([int(query_id) for query_id in query_ids])
    is_valid = (ids == query_int_ids)
    if is_valid:
        return "valid"
    return "non_valid"


def groupby_and_count(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Groupby dataframe by valid-column, date and evant-type.

    Args:
        dataframe (pd.DataFrame).

    Returns:
        (pd.DataFrame).

    """
    dataframe_grouped = dataframe.groupby(['is_valid', dataframe['timestamp'].dt.date, 'event_type'])
    return dataframe_grouped[['ids']].count().rename(columns={'ids': 'count'})


class LogProcessing:

    def __init__(self, path_to_logs_zip: str):
        """Initialize logger, path to zipped data, path to file inside zipped data.

        Args:
            path_to_file (str): full or relative path to file.

        Examples:
            >>> LogProcessing("./test_files.zip")

        """
        self.logger = logging.getLogger(__name__)
        self.path_to_zip = path_to_logs_zip
        self.logger.debug(f"Path to zip is {self.path_to_zip}")

    def read_zip_file(self) -> pd.DataFrame:
        """Read logs from zipped file.

        The path to zip is in self.path_to_zip, file path inside zipped data is in self.path_to_file.


        Returns:
            (list): list with logs in dict format.

        """
        logs = pd.DataFrame()
        with ZipFile(self.path_to_zip) as zip_file:
            file_pathes = sorted([path for path in zip_file.namelist() if not path.endswith(os.sep)])
            self.logger.debug(f"files in {self.path_to_zip} are: {file_pathes}")
            for log_path in file_pathes:
                self.logger.debug(f"{log_path} is in process")
                with zip_file.open(log_path) as log_file:
                    logs_to_add = pd.read_json(log_file, lines=True)
                    logs = pd.concat([logs, logs_to_add], ignore_index=True)
        self.logger.debug("Result DataFrame is ready")
        return logs

    def parse_logs(self, logs: pd.DataFrame) -> pd.DataFrame:
        """Parse logs for amount of valid logs, grouped result by timestamp and event_type

        Args:
            logs (pd.DataFrame).

        Returns:
            pd.DataFrame.

        """
        self.logger.info("Creation of is_valid field is in process")
        logs['is_valid'] = logs.apply(create_is_valid_field, axis=1)
        self.logger.info("Group by columns and count is in process")
        return groupby_and_count(logs)
