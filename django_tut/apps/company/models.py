import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):

    name = models.TextField(_("company name"))
    phone_number = models.TextField(_("phone number"), null=True)
    site = models.TextField(_("site"), null=True)

    created_at = models.DateTimeField(_("created at"))
    updated_at = models.DateTimeField(_("updated at"))

    class Meta:
        db_table = "company"

    @classmethod
    def get_company(cls, pk):
        return Company.objects.get(pk=pk)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        return super(Company, self).save(*args, **kwargs)
