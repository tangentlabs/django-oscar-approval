from django.views import generic
from django.db.models import get_model
from django.conf import settings

Line = get_model('order', 'Line')


class AccountSummaryApprovalMixin(object):

    def get_account_approval_context_data(self):
        ctx = {
            'approval_item_number': (Line.objects.filter(
                                    status=settings.OSCAR_LINE_APPROVAL_STATUS)
                                    .count())
        }
        return ctx
