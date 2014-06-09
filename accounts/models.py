import warnings

from django.core.exceptions import ImproperlyConfigured

from django.core.mail import send_mail

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, SiteProfileNotAvailable, PermissionsMixin)
from django.utils import timezone

from django.utils.http import urlquote


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.OneToOneField('products.Product')
    quantity = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)


class Address(models.Model):
    number = models.IntegerField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)


class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        return self._create_user(email, first_name, last_name, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        return self._create_user(email, first_name, last_name, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)

    address = models.ManyToManyField(Address, null=True)
    phone = models.CharField(max_length=10)
    cart = models.ForeignKey(Cart, null=True)

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin '
                                             'site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/accounts/%s/" % urlquote(self.username)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn("The use of AUTH_PROFILE_MODULE to define user profiles has been deprecated.",
                      DeprecationWarning, stacklevel=2)
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings

            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                    self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache


class Customer_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
<<<<<<< HEAD
    order_date = models.DateTimeField()
=======
>>>>>>> 3988bb483a692b890a9972ae661314ce133bbb0b
    customer_email = models.OneToOneField('accounts.User')
    product = models.ForeignKey('accounts.Cart')
    status = models.CharField(max_length=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)