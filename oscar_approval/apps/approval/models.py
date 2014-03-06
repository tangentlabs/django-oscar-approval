from abstract_models import AbstractOrderLineApprovalLog


class OrderLineApprovalLog(AbstractOrderLineApprovalLog):

    pass

from .signals import order_line_approved, order_line_rejected
from .receivers import receive_order_line_approved, receive_order_line_rejected

order_line_approved.connect(receive_order_line_approved)
order_line_rejected.connect(receive_order_line_rejected)
