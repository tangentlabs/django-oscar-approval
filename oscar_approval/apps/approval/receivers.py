from django.db.models import get_model

from .abstract_models import APPROVE, REJECT


def receive_order_line_approved(sender, line, user, **kwargs):
    OrderLineApprovalLog = get_model('approval', 'OrderLineApprovalLog')
    OrderLineApprovalLog.objects.create(line=line, user=user, event_type=APPROVE)


def receive_order_line_rejected(sender, line, user, **kwargs):
    OrderLineApprovalLog = get_model('approval', 'OrderLineApprovalLog')
    OrderLineApprovalLog.objects.create(line=line, user=user, event_type=REJECT)
