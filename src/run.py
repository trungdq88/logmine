import sys
from .log_mine import LogMine
from .cli_input import Input


def run():
    inp = Input()

    if len(sys.argv) == 1 and sys.stdin.isatty():
        inp.print_help()
        return

    options = inp.get_args()

    if not sys.stdout.isatty():
        # Disable all highlighting options
        options['highlight_patterns'] = False
        options['highlight_variables'] = False

    input_files = options['file']

    logmine = LogMine(
        # Processor config
        {k: options[k] for k in (
            'single_core',
        )},
        # Cluster config
        {k: options[k] for k in (
            'max_dist',
            'variables',
            'delimeters',
            'min_members',
            'k1',
            'k2',
        )},
        # Output config
        {k: options[k] for k in (
            'sorted',
            'number_align',
            'pattern_placeholder',
            'mask_variables',
            'highlight_patterns',
            'highlight_variables',
        )},
    )

    return logmine.run(input_files)
