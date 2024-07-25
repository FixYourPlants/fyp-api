from factory import SubFactory, Faker, Iterator, post_generation
from factory.django import DjangoModelFactory, ImageField

from app.plants.models import Plant, Difficulty, History, Opinion, Characteristic
from app.sickness.tests.factories import SicknessFactory
from app.users.tests.factories import UserFactory


class CharacteristicFactory(DjangoModelFactory):
    class Meta:
        model = Characteristic

    # Attributes
    id = Faker('uuid4')
    name = Faker('word')


class PlantFactory(DjangoModelFactory):
    class Meta:
        model = Plant

    id = Faker('uuid4')
    name = Faker('word')
    scientific_name = Faker('word')
    description = Faker('text', max_nb_chars=500)
    image = ImageField(color='green', width=800, height=600, format='jpeg', null=True, blank=True)
    difficulty = Iterator([tag for tag in Difficulty])
    treatment = Faker('text', max_nb_chars=500)

    @post_generation
    def sickness(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for sickness in extracted:
            self.sickness.set(sickness)

    @post_generation
    def characteristics(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for characteristic in extracted:
            self.characteristics.set(characteristic)

    @post_generation
    def notifications(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for notification in extracted:
            self.notifications.set(notification)
class HistoryFactory(DjangoModelFactory):
    class Meta:
        model = History

    # Attributes
    id = Faker('uuid4')
    created_at = Faker('date_time_this_year', before_now=True, after_now=False, tzinfo=None)
    image = ImageField(color='gray', width=800, height=600, format='jpeg', null=True, blank=True)

    # Relationships
    plant = SubFactory(PlantFactory)
    sickness = SubFactory(SicknessFactory, null=True)

class OpinionFactory(DjangoModelFactory):
    class Meta:
        model = Opinion

    # Attributes
    id = Faker('uuid4')
    title = Faker('sentence', nb_words=4)
    description = Faker('text', max_nb_chars=500)
    created_at = Faker('date_time_this_year', before_now=True, after_now=False, tzinfo=None)

    # Relationships
    plant = SubFactory(PlantFactory)
    user = SubFactory(UserFactory)
