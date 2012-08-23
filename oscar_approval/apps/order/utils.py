from django.conf import settings


class OrderCreatorApprovalMixin(object):

    def update_line_approval_extra_fields(self, order, basket_line, extra_line_fields):

        """
            Updates line additional data with stuff related to order approval.
            Can be used in a class inheriting from oscar's OrderCreator
            in the 'create_line_models' method:

        """

        if basket_line.product.requires_approval:
            if extra_line_fields is None:
                extra_line_fields = {}
        extra_line_fields['status'] = settings.OSCAR_LINE_APPROVAL_STATUS
        order.status = settings.OSCAR_ORDER_APPROVAL_STATUS
        order.save()
        return extra_line_fields

