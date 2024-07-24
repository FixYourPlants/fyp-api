
import factory
from factory.django import DjangoModelFactory
from pytz import timezone

from app.notification.models import Notification


class NotificationFactory(DjangoModelFactory):
    class Meta:
        model = Notification

    id = factory.Faker('uuid4')
    title = factory.Faker('sentence', nb_words=5)
    timestamp = factory.Faker('date_time_this_year', before_now=True, after_now=False, tzinfo=timezone('UTC'))
    description = factory.Faker('text', max_nb_chars=500)
