from django.views import generic
from django.db.models import get_model
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from . import signals

Line = get_model('order', 'Line')


class OrderLineApprovalListView(generic.ListView):

    template_name = 'oscar_approval/order_line_approval_list.html'
    model = Line

    def get_queryset(self):
        return self.model.objects.filter(
                    status=settings.OSCAR_LINE_APPROVAL_STATUS)


class OrderLineApproveView(generic.UpdateView):

    model = Line

    def post(self, request, *args, **kwargs):
        signals.order_line_approved.send(sender=self,
                                         line=self.get_object(),
                                         user=request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('approval:order-line-approval-list')


class OrderLineRejectView(generic.UpdateView):

    model = Line

    def post(self, request, *args, **kwargs):
        signals.order_line_rejected.send(sender=self,
                                         line=self.get_object(),
                                         user=request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('approval:order-line-approval-list')
