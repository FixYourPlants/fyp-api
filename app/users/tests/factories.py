from django.contrib.auth.hashers import make_password
from factory import Sequence, Faker, LazyFunction, post_generation
from factory.django import DjangoModelFactory, ImageField

from app.users.models import User


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('username',)

    # Attributes
    id = Faker('uuid4')
    username = Sequence(lambda n: f'testuser{n}')
    password = LazyFunction(lambda: make_password('password'))
    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    is_active = True
    is_staff = False
    image = ImageField(color='blue', width=800, height=800, format='jpeg', default='users/default.png')
    about_me = Faker('text', max_nb_chars=200)
    email_verified = False
    googleAccount = False

    @post_generation
    def favourite_plant(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for plant in extracted:
            self.favourite_plant.add(plant)

    @post_generation
    def affected_sicknesses(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for sickness in extracted:
            self.affected_sicknesses.add(sickness)

    @post_generation
    def history(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        for history_item in extracted:
            self.history.add(history_item)
