from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from products.models import Product


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    # customer_id = models.OneToOneField(User)
    product_id = models.OneToOneField(Product)
    quantity = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)


class Address(models.Model):
    number = models.IntegerField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)


class User(AbstractBaseUser):
    # id = models.AutoField(primary_key=True)
    # email = models.EmailField(max_length=30, unique=True)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    address = models.ManyToManyField(Address)
    phone = models.IntegerField()
    cart = models.OneToOneField(Cart)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # def get_full_name(self):
    #     return self.first_name + " " + self.last_name
    #
    # def get_short_name(self):
    #     return self.first_name


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

    def order(self):
        pass
        # cur cart to order
        # user's cart point to new empty cart


class Customer_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.OneToOneField('User')
    product = models.ForeignKey('Cart')
    status = models.CharField(max_length=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)