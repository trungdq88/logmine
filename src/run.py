from LogMine import LogMine
from Input import Input


def run():
    inp = Input()
    options = inp.get_args()

    if len(options['file']) == 0:
        inp.print_help()
        return

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
            'highlight_patterns',
            'mask_variables',
            'highlight_variables',
        )},
    )

    logmine.run(options['file'])

run()
