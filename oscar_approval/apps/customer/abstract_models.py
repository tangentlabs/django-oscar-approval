from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractProfile(models.Model):

    is_order_approver = models.BooleanField(_('Has permissions to approve orders'),
                                            default=False)

    class Meta:
        abstract = True
