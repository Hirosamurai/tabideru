
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_name = models.CharField(max_length=30, verbose_name="苗字")
    first_name = models.CharField(max_length=30, verbose_name="名前")
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='ホテル写真')
    address = models.CharField(max_length=1000)
    price = models.IntegerField()
    information = models.TextField()


    class Meta:
        verbose_name_plural = 'ホテル'

    def __str__(self):
        return self.hotel_name



class Mylist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True)
    restaurant = models.CharField(max_length=100, null=True, blank=True)
    list_name = models.CharField(max_length=40, )
    class Meta:
        verbose_name_plural = 'マイリスト'

    def __str__(self):
        return self.list_name
