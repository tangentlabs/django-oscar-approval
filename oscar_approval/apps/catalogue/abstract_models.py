from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractProduct(models.Model):

    requires_approval = models.BooleanField(_("Requires authorisation"), default=False)

    class Meta:
        abstract = True
