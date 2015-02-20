"""
Models module that contains model classes and helper objects to crete better user accounts.
"""
from django.db import models

from django.contrib.auth.models import AbstractUser

from household.models import Household
from common.utils import upload_to_callable


USER_TYPES = (
    ("manager", "Household Manager"),
    ("member", "Household Member")
)

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class HouseholdUser(AbstractUser):
    """
    Modified user model with two extra fields, household and user_type.
    Household field determines to which household user belongs.
    User_type filed determines type of user (manager or regular member).
    """

    household = models.ForeignKey(Household, null=True, default=None, related_name="members")
    user_type = models.TextField(choices=USER_TYPES, null=True, blank=False)
    photo = models.ImageField(upload_to=upload_to_callable, default=None, storage=OverwriteStorage())

    def is_manager(self):
        """
        Checks if user is household manager.
        """
        return self.user_type == "manager"

    def is_member(self):
        """
        Checks if user is household member.
        """
        return self.user_type == "member"

    @classmethod
    def get_users_from_household(cls, household):
        """
        Returns values queryset for users from household.
        """
        if household is not None:
            return cls.objects.filter(household=household).values('id', 'first_name', 'last_name', 'user_type')
        else:
            return None
