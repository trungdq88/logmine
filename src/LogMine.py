from Processor import Processor
from Output import Output


class LogMine():
    def __init__(self, processor_config, cluster_config, output_options):
        self.processor = Processor(processor_config, cluster_config)
        self.output = Output(output_options)

    def run(self, files):
        clusters = self.processor.process(files)
        self.output.out(clusters)
