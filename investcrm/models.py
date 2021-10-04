from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    add_ln1 = models.CharField(max_length=100, null=True)
    add_ln2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=185, null=True)
    state = models.CharField(max_length=30, null=True)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
