from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

import os


class Client(models.Model):
    api_key = models.TextField(unique=True, blank=True)
    app_name = models.TextField()
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{0}:{1}".format(self.user.username, self.app_name)

    def _keygen(self, length):
        alphabet = ('0123456789'
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyz')

        junk = os.urandom(20)
        key = [alphabet[ord(j) % len(alphabet)] for j in junk]
        return ''.join(key)

    def save(self, *args, **kwargs):
        while True:
            if len(self.api_key) == 0:
                self.api_key = self._keygen(20)

            objs = Client.objects.filter(api_key=self.api_key)
            if len(objs) == 0:
                return super(Client, self).save(*args, **kwargs)
            else:
                self.api_key = ''


class Counter(models.Model):
    name = models.TextField(unique=True)
    count = models.PositiveIntegerField(default=0)
    last_modified = models.DateField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u"{0}:{1}".format(self.name, self.count)

    def increment(self):
        if self.last_modified < now().date():
            self.count = 1
        else:
            self.count += 1
        self.save()

    def reset(self):
        self.count = 0
        self.save()
