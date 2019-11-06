from LogMine import LogMine
from Output import Output


VARIABLES = [
    # ('<ip>', '\\d{3}\\.\\d{3}\\.\\d{3}\\.\\d{3}'),
    ('<date>', '\\d{4}-\\d{2}-\\d{2}'),
    ('<time>', '\\d{2}:\\d{2}(:\\d{2})?'),
    ('<number>', '\\d+'),
    ('<email>', '\\w+@\\.\\w+'),
    ('<version_number>', 'v\\d+\\.\\d+\\.\\d+'),
]

DELIMETERS = '\\s'


if __name__ == '__main__':
    # f = 'big.log'
    # f = 'Linux_2k.log'
    f = '/Users/tdinh/desktop-archives/2019-11-02/sentry_logs/home/sentry/logs/sentry-worker.log'
    cluster_config = {
        'max_dist': 0.7,
        'variables': [],
        'delimeters': '\\s',
        'min_members': 2,
        'k1': 1,
        'k2': 1,
    }
    output_options = {
        'sorted': 'desc',
        'number_align': True,
        'pattern_placeholder': None,
        'highlight_patterns': True,
        'mask_variables': True,
        'highlight_variables': True,
    }
    processor_config = {
        'single_core': False
    }
    clusters = LogMine(
        processor_config,
        cluster_config,
        output_options
    ).run(f)
