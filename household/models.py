from django.db import models


# Create your models here.
class Household(models.Model):
    """
    Model that represents household. It has name and address field so that we can
    differentiate households.
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'address')

    def __unicode__(self):
        return "%s (Address: %s)" % (self.name, self.address)
