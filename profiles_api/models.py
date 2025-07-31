from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    # django-cli 用来穿管用户的方法
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super(self, email, name, password=None):
        """Create a new super with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 因为django cli默认是和默认的用户模型打交道的
    # 我们自己定了用户模型后, 就需要告诉django-cli怎么和我们的模型打交道
    objects = UserProfileManager()
    USERNAME_FIELD = 'email' # 我们用 email 字段替换了默认的username字段
    REQUIRED_FIELD = ['name'] # 制定了哪些字段是必须字段

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string reprensation of user"""
        return self.email
