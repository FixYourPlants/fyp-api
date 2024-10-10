from factory import Faker, post_generation
from factory.django import DjangoModelFactory, ImageField

from app.sickness.models import Sickness


class SicknessFactory(DjangoModelFactory):
    class Meta:
        model = Sickness

    # Attributes
    id = Faker('uuid4')
    name = Faker('word')
    description = Faker('text', max_nb_chars=500)
    treatment = Faker('text', max_nb_chars=500)
    image = ImageField(color='red', width=800, height=600, format='jpeg', null=True, blank=True)

    @post_generation
    def notifications(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.notifications.set(extracted)
