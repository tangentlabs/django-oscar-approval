from django.db.models import get_model

from oscar_approval.apps.approval.models import (OrderLineApprovalLog,
                                                 APPROVE, REJECT)


def receive_order_line_approved(sender, line, user, **kwargs):
    OrderLineApprovalLog.objects.create(line=line, user=user, event_type=APPROVE)


def receive_order_line_rejected(sender, line, user, **kwargs):
    OrderLineApprovalLog.objects.create(line=line, user=user, event_type=REJECT)
