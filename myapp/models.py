from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, User
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None,name=None):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        print(password)
        user.name = name
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None,name=None):
        user = self.create_user(email=email, password=password,name=name)
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def save(self, *args, **kwargs):
        user = super(MyUserManager, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user
    def get_by_natural_key(self, email):
        return self.get(email=email)

class Board(models.Model):
    name = models.CharField(max_length=300, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')

    # lists = models.ManyToManyField('List', related_name='lists')

class List(models.Model):
    title = models.CharField(max_length=300, null=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')

class Card(models.Model):
    description = models.CharField(max_length=500, null=False, default="")
    title = models.CharField(max_length=500, null=False, default="")
    order = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')

