import argparse


class Input():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='LogMine: a log pattern analyzer'
        )

        parser.add_argument(
            'file',
            default=['-'],
            type=str,
            nargs='*',
            help='Filenames or glob pattern to analyze. Default: stdin'
        )

        parser.add_argument(
            '-m',
            '--max-dist',
            default=0.6,
            type=float,
            help="""
            This parameter control how the granularity of the clustering
            algorithm.  Lower the value will provide more granular clusters
            (more clusters generated). Default: 0.6
            """
        )

        parser.add_argument(
            '-v',
            '--variables',
            default=[],
            nargs='*',
            type=str,
            help="""
            List of variables to replace before process the log file. A
            variable is a pair of name and a regex pattern. Format:
            "name:/regex/". During processing time, LogMine will consider all
            texts that match varible regexes to be the same value. This is
            useful to reduce the number of unnecessary cluster generated, with
            trade off of processing time. Default: None
            """
        )

        parser.add_argument(
            '-d',
            '--delimeters',
            default='\\s+',
            type=str,
            help="""
            A regex pattern used to split a line into multiple fields.
            Default: "\\s+"
            """
        )

        parser.add_argument(
            '-i',
            '--min-members',
            default=2,
            type=int,
            help="""
            Minimum number of members in a cluster to show in the result.
            Default: 2
            """
        )

        parser.add_argument(
            '-k1',
            '--fixed-value-weight',
            dest='k1',
            default=1,
            type=float,
            help="""
            Internal weighting variable. This value will be used as the weight
            value when two fields have the same value. This is used in the
            score function to calculate the distance between two lines.
            Default: 1
            """
        )

        parser.add_argument(
            '-k2',
            '--variable-weight',
            dest='k2',
            default=1,
            type=float,
            help="""
            Similar to k1 but for comparing variables. Two variable is
            considering the same if they have same name.
            Default: 1
            """
        )

        parser.add_argument(
            '-s',
            '--sorted',
            default='desc',
            type=str,
            choices=['desc', 'asc'],
            help="""
            Sort the clusters by number of members.
            Default: desc
            """
        )

        parser.add_argument(
            '-da',
            '--disable-number-align',
            dest='number_align',
            action='store_false',
            default=True,
            help="""
            Disable number align in output. Default: True
            """
        )

        parser.add_argument(
            '-p',
            '--pattern-placeholder',
            default=None,
            type=str,
            help="""
            Use a string as placeholder for patterns in output. Default: None
            """
        )

        parser.add_argument(
            '-dhp',
            '--disable-highlight-patterns',
            dest='highlight_patterns',
            default=True,
            action='store_false',
            help="""
            Disable highlighting for patterns in output. Default: True
            """
        )

        parser.add_argument(
            '-dm',
            '--disable-mask-variables',
            dest='mask_variables',
            default=True,
            action='store_false',
            help="""
            Disable masks for variables in output. When disabled variables
            will be shown as the actual value. Default: True
            """
        )

        parser.add_argument(
            '-dhv',
            '--disable-highlight-variables',
            dest='highlight_variables',
            default=True,
            action='store_false',
            help="""
            Disable highlighting for variables in output. Default: True
            """
        )

        parser.add_argument(
            '-c',
            '--single-core',
            default=False,
            action='store_true',
            help="""
            Force LogMine to only run on 1 core. This will increase the
            processing time. Note: the result output can be different
            compare to when run with multicores, this is expected.
            Default: False
            """
        )

        self.parser = parser

    def get_args(self):
        return vars(self.parser.parse_args())

    def print_help(self):
        return self.parser.print_help()


"""
Examples:

    -v  email:/\\w+@\\.\\w+/ \
        version_number:/v\\d+\\.\\d+\\.\\d+/ \
        date:/\\d{4}-\\d{2}-\\d{2}/
"""
