"""
Logs parsing; groupby it by validity, date and type of event; count wrt result groups.
For more details see the link:

https://gist.github.com/VerusK/acdd4ae70419aa15bb1c60a4809e4cc2

copyright: (c) 2019 by Artem Kozlov.

"""


import logging

from ArgumentParser import ArgumentParser
from parsers.LogProcessing import LogProcessing
from util import get_config, logger_initializing, save_result


PATH_TO_CONFIG = "./configs/config.yaml"
CONFIG = get_config(PATH_TO_CONFIG)
BASH_ARGUMENTS = ArgumentParser().get_arguments()
PATH_TO_RESULT = CONFIG["path_to_result"]


def main():
    logger_initializing(CONFIG["path_to_logger"])
    logger = logging.getLogger(__name__)
    try:
        log_processing = LogProcessing(BASH_ARGUMENTS["path_to_zip"])
        logs = log_processing.read_zip_file()
        result_logs = log_processing.parse_logs(logs)
        save_result(result_logs, PATH_TO_RESULT)
        if BASH_ARGUMENTS["print"]:
            print(result_logs)
    except Exception as e:
        logger.debug(str(e))
        raise e


if __name__ == "__main__":
    main()
