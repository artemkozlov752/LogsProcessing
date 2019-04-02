import argparse


DEFAULT_PATH = "./logs.zip"
DEFAULT_PRINT_OPTION = False


class ArgumentParser(object):
    """Parser of bash path argument."""

    def get_arguments(self) -> str:
        """Parse bash arguments for path to zip file.

        Returns:
            (str): path to zip with log files.

        """
        parser = self.prepare_parser()
        arguments = vars(parser.parse_args())

        return arguments

    @staticmethod
    def prepare_parser():
        """Prepare parser of bash arguments.

        Returns:
            Parser with path-argument.

        """
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--path_to_zip',
            default=DEFAULT_PATH,
            type=str,
            help='path to zip file with logs'
        )
        parser.add_argument(
            '--print',
            default=DEFAULT_PRINT_OPTION,
            action='store_true',
            help='if true print to console'
        )
        return parser
