from django.views import generic
from django.db.models import get_model

Line = get_model('order', 'Line')


class OrderLineApprovalList(generic.ListView):

    template_name = 'oscar_approval/order_line_approval_list.html'
    model = Line
