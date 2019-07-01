import factory
import factory.fuzzy
from vng_api_common.constants import RolOmschrijving, RolTypes

from ...models import RolType
from .zaken import ZaakTypeFactory


class RolTypeFactory(factory.django.DjangoModelFactory):
    zaaktype = factory.SubFactory(ZaakTypeFactory)

    omschrijving = factory.Faker('text', max_nb_chars=20)
    omschrijving_generiek = factory.fuzzy.FuzzyChoice(choices=RolOmschrijving.values)

    class Meta:
        model = RolType


class MogelijkeBetrokkeneFactory(factory.django.DjangoModelFactory):

    roltype = factory.SubFactory(RolTypeFactory)
    betrokkene = factory.Faker('url')
    betrokkene_type = factory.fuzzy.FuzzyChoice(choices=RolTypes.values)

    class Meta:
        model = 'datamodel.MogelijkeBetrokkene'
