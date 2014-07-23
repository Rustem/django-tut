from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):

    name = models.TextField(_("company name"))
    phone_number = models.TextField(_("phone number"), null=True)
    site = models.TextField(_("site"), null=True)

    class Meta:
        db_table = "company"
