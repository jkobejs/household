"""
Module that provides managers for Transaction model.
"""
from django.db import models


# Todo: remove if not needed
class TransactionManager(models.Manager):
    """
    Manager that provides some specific methods for retrieving transactions data.
    """
    def objects(self):
        """
        Dummy method.
        """
        return self.objects()
