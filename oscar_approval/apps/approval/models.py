from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


APPROVE, REJECT = 'Approve', 'Reject'


class OrderLineApprovalLog(models.Model):

    EVENT_TYPE_CHOICES = (
        (APPROVE, _("Item approved")),
        (REJECT, _("Item rejected")),
    )

    line = models.ForeignKey('order.Line')
    user = models.ForeignKey(User)
    event_date = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=20)



from oscar_approval.apps.approval.signals import (order_line_approved,
                                                  order_line_rejected)
from oscar_approval.apps.approval.receivers import (receive_order_line_approved,
                                                    receive_order_line_rejected)

order_line_approved.connect(receive_order_line_approved)
order_line_rejected.connect(receive_order_line_rejected)