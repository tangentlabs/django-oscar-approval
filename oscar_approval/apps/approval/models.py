from abstract_models import AbstractOrderLineApprovalLog


class OrderLineApprovalLog(AbstractOrderLineApprovalLog):

    pass



from oscar_approval.apps.approval.signals import (order_line_approved,
                                                  order_line_rejected)
from oscar_approval.apps.approval.receivers import (receive_order_line_approved,
                                                    receive_order_line_rejected)

order_line_approved.connect(receive_order_line_approved)
order_line_rejected.connect(receive_order_line_rejected)