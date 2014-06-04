from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from products.models import Product


class Address(models.Model):
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    postcode = models.CharField(max_length=225)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.ManyToManyField(Address)
    phone = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Please fill an email address')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey('User')
    status = models.CharField(max_length=10)
    total = models.FloatField()


class Customer_Order_Product(models.Model):
    order_id = models.ForeignKey('Customer_Order')
    product_id = models.ForeignKey('products.Product', primary_key=True)
    quantity = models.IntegerField()