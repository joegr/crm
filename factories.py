import factory
from factory.django import DjangoModelFactory
from investcrm.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Faker('email')
    email = username
    password = factory.LazyFunction(lambda: make_password('chess64'))


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    user = factory.SubFactory(UserFactory)
    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    email = user
    add_ln1 = factory.Faker('address')
    add_ln2 = factory.Faker('address')
    city = factory.Faker('city')
    state = factory.Faker('state')
