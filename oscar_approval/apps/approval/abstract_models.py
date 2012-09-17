from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


APPROVE, REJECT = 'Approve', 'Reject'


class AbstractOrderLineApprovalLog(models.Model):

    EVENT_TYPE_CHOICES = (
        (APPROVE, _("Item approved")),
        (REJECT, _("Item rejected")),
    )

    line = models.ForeignKey('order.Line')
    user = models.ForeignKey(User)
    event_date = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=30)

    class Meta:
        abstract = True