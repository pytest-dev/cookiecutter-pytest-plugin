from nomad.datamodel.data import EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Package, Quantity

m_package = Package()


class ExampleSection(EntryData):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        logger.info('ExampleSection.normalize called')

        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
