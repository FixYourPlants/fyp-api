from factory import Faker, SubFactory
from factory.django import DjangoModelFactory, ImageField

from app.diary.models import Diary, Page


class DiaryFactory(DjangoModelFactory):
    class Meta:
        model = Diary

    # Attributes
    id = Faker('uuid4')
    title = Faker('sentence', nb_words=4)
    updated_at = Faker('date_time_this_decade', before_now=True, after_now=False, tzinfo=None)

    # Relationships
    plant = SubFactory('app.plants.tests.factories.PlantFactory')
    user = SubFactory('app.users.tests.factories.UserFactory')

class PageFactory(DjangoModelFactory):
    class Meta:
        model = Page

    # Attributes
    id = Faker('uuid4')
    title = Faker('sentence', nb_words=6)
    content = Faker('text', max_nb_chars=2000)
    created_at = Faker('date_time_this_year', before_now=True, after_now=False, tzinfo=None)
    image = ImageField(color='blue', width=800, height=600, format='jpeg')

    # Relationships
    diary = SubFactory(DiaryFactory)

