from .processor import Processor
from .output import Output
from .debug import log


class LogMine():
    def __init__(self, processor_config, cluster_config, output_options):
        log(
            "LogMine: init with config:",
            processor_config,
            cluster_config, output_options
        )
        self.processor = Processor(processor_config, cluster_config)
        self.output = Output(output_options)

    def run(self, files):
        log("LogMine: run with files:", files)
        clusters = self.processor.process(files)
        log("LogMine: output cluster:", clusters)
        self.output.out(clusters)
