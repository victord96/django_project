from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """ Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """ Create New User """
        if not email:
            raise ValueError('The user needs to have an email')

        email = self.normalize_email(email)
        user = self.model(email= email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model of BBDD for users in the sistem
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Obtain fullname of user"""
        return self.name

    def get_short_name(self):
        """ Obtain short name of user"""
        return self.name

    def __str__(self) -> str:
        """ Return string that represents our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """ Update of status profile """  
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return model like char """
        return self.status_text