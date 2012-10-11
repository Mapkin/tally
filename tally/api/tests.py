"""
Unit tests for the API application.
"""

from django.contrib.auth.models import User
from django.test import TestCase
from tally.api.models import Client, Counter

import datetime
import time


class ClientTest(TestCase):
    def test_create(self):
        user = User.objects.create_user('test', 'test')

        client = Client(user=user, app_name='Terrible App')
        client.save()

        self.assertEqual(len(client.api_key), 20)
        self.assertEqual(client.user.id, user.id)

    def test_uniqueness(self):
        user1 = User.objects.create_user('user1', 'xxx')
        client1 = Client(user=user1, app_name='Cromulent', api_key='derp')
        client1.save()

        user2 = User.objects.create_user('user2', 'xxx')
        client2 = Client(user=user2, app_name='Fungible', api_key='derp')
        client2.save()


class CounterTest(TestCase):
    def test_increment_with_today(self):
        today = datetime.date.today()
        counter = Counter(name="test", last_modified=today)
        print counter
        counter.increment()
        self.assertEqual(counter.count, 1)

    def test_increment_with_yesterday(self):
        yesterday = datetime.date.fromtimestamp(time.time()-60*60*24)
        counter = Counter(name="test", count=1, last_modified=yesterday)
        counter.increment()
        self.assertEqual(counter.count, 1)

    def test_reset(self):
        counter = Counter(name="test", count=7)
        counter.reset()
        self.assertEqual(counter.count, 0)
