# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _

# choice_bal = [
#     (10, 10),
#     (15, 15),
#     (25, 25),
#     (50, 50),
#     (75, 75),
#     (100, 100),
# ]


# class Trader(models.Model):
#     user_name = models.CharField(max_length=30, verbose_name='User Name', blank=True, default='Name')

#     admin = models.BooleanField(default=False, verbose_name='Trader active')
#     link = models.CharField(max_length=355, verbose_name='link trader profile')

#     # admin_leverage = models.PositiveIntegerField(verbose_name='Admin default leverage', default=10)

#     # api_key = models.CharField(max_length=265, verbose_name='api_key', blank=True)
#     # api_secret = models.CharField(max_length=265, verbose_name='api_secret', blank=True)

#     def __str__(self):
#         return self.user_name

#     class Meta:
#         verbose_name = 'Trader'
#         verbose_name_plural = 'Traders'


# class User(AbstractUser):
#     email = models.EmailField(
#         _('email address'),
#         unique=True,
#     )

#     email_verify = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     balance_per = models.IntegerField(verbose_name='Balance percent per trade', default=10, choices=choice_bal)
#     leverage = models.IntegerField(verbose_name='Default leverage', default=10,
#                                    validators=[
#                                        MaxValueValidator(100),
#                                        MinValueValidator(1)
#                                    ]
#                                    )
#     subs_date_end = models.DateField(null=True, verbose_name='End of subscription', blank=True)

#     subs_active = models.BooleanField(default=False,
#                                       verbose_name='If the subscription is active then true if not false')

#     api_key = models.CharField(max_length=265, verbose_name='api_key', blank=True)
#     api_secret = models.CharField(max_length=265, verbose_name='api_secret', blank=True)

#     trader = models.OneToOneField(Trader, on_delete=models.CASCADE, blank=True, null=True)

#     def __str__(self):
#         return self.first_name


# class Order(models.Model):
#     trader_name = models.ForeignKey(Trader, on_delete=models.CASCADE)

#     symbol = models.CharField(max_length=15, verbose_name='Symbol')
#     side = models.CharField(max_length=55, verbose_name='SIDE', default='none')
#     size = models.CharField(max_length=55, verbose_name='Size')
#     entry_price = models.CharField(max_length=55, verbose_name='Entry Price')
#     mark_price = models.CharField(max_length=55, verbose_name='Mark Price')
#     pnl = models.CharField(max_length=55, verbose_name='PNL (ROE %)')
#     date = models.CharField(max_length=55, verbose_name='TIME')
#     is_active = models.BooleanField(default=True)
#     upd = models.CharField(max_length=86, verbose_name='Update time order')

#     def __str__(self):
#         return f'{self.trader_name}/{self.symbol}'

#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'

import auto_prefetch
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from Users.helpers import TimeBasedModel

choice_bal = [
    (10, 10),
    (15, 15),
    (25, 25),
    (50, 50),
    (75, 75),
    (100, 100),
]


class Trader(models.Model):
    user_name = models.CharField(max_length=30, verbose_name='User Name', blank=True, default='Name')

    admin = models.BooleanField(default=False, verbose_name='Trader active')
    link = models.CharField(max_length=355, verbose_name='link trader profile')

    admin_leverage = models.PositiveIntegerField(verbose_name='Admin default leverage', default=10)

    api_key = models.CharField(max_length=265, verbose_name='api_key', blank=True)
    api_secret = models.CharField(max_length=265, verbose_name='api_secret', blank=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Trader'
        verbose_name_plural = 'Traders'

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(TimeBasedModel, AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    about = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(verbose_name="email address", unique=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    balance_per = models.IntegerField(verbose_name='Balance percent per trade', default=10, choices=choice_bal)
    leverage = models.IntegerField(verbose_name='Default leverage', default=10,
                                   validators=[
                                       MaxValueValidator(100),
                                       MinValueValidator(1)
                                   ]
                                   )
    subs_date_end = models.DateField(null=True, verbose_name='End of subscription', blank=True)

    subs_active = models.BooleanField(default=False,
                                      verbose_name='If the subscription is active then true if not false')

    api_key = models.CharField(max_length=265, verbose_name='api_key', blank=True)
    api_secret = models.CharField(max_length=265, verbose_name='api_secret', blank=True)

    trader = models.OneToOneField(Trader, on_delete=models.CASCADE, blank=True, null=True)


    verified = models.BooleanField(default=False)

    objects = UserManager()

    class Meta(auto_prefetch.Model.Meta):
        ordering = ["first_name", "last_name"]
        verbose_name = "user"

    def __str__(self):
        return self.get_full_name() or self.email


class Order(models.Model):
    trader_name = models.ForeignKey(Trader, on_delete=models.CASCADE)

    symbol = models.CharField(max_length=15, verbose_name='Symbol')
    side = models.CharField(max_length=55, verbose_name='SIDE', default='none')
    size = models.CharField(max_length=55, verbose_name='Size')
    entry_price = models.CharField(max_length=55, verbose_name='Entry Price')
    mark_price = models.CharField(max_length=55, verbose_name='Mark Price')
    pnl = models.CharField(max_length=55, verbose_name='PNL (ROE %)')
    date = models.CharField(max_length=55, verbose_name='TIME')
    is_active = models.BooleanField(default=True)
    upd = models.CharField(max_length=86, verbose_name='Update time order')

    def __str__(self):
        return f'{self.trader_name}/{self.symbol}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'