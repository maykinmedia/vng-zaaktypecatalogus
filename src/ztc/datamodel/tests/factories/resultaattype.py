import factory
import factory.fuzzy

from ...models import ResultaatType
from .zaken import ZaakTypeFactory


class ResultaatTypeFactory(factory.django.DjangoModelFactory):
    zaaktype = factory.SubFactory(ZaakTypeFactory)
    omschrijving = factory.Faker('word', locale='nl')
    omschrijving_generiek = factory.Faker('url')
    _omschrijving_generiek = factory.Faker('word')
    selectielijstklasse = factory.Faker('url')
    archiefnominatie = factory.fuzzy.FuzzyChoice(['blijvend_bewaren', 'vernietigen'])

    datum_begin_geldigheid = factory.SelfAttribute('zaaktype.datum_begin_geldigheid')

    class Meta:
        model = ResultaatType
