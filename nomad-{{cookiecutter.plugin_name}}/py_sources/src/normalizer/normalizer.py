from nomad.datamodel.metainfo.workflow import Workflow
from nomad.normalizing import Normalizer


class ExampleNormalizer(Normalizer):
    domain = None

    def normalize(self, logger):
        super().normalize(logger)
        logger.info('ExampleNormalizer called')

        self.entry_archive.workflow2 = Workflow(name='Example workflow')
