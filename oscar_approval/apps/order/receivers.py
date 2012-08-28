from django.conf import settings


def receive_order_placed(sender, order, user, **kwargs):
    authorisation_required = False
    for line in order.lines.all():
        if line.product.requires_approval:
            line.status = settings.OSCAR_LINE_APPROVAL_STATUS
            line.save()
            authorisation_required = True

    if authorisation_required:
        order.status = settings.OSCAR_ORDER_APPROVAL_STATUS
        order.save()
