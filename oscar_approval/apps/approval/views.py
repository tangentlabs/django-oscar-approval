from django.views import generic
from django.db.models import get_model
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from . import signals, forms

Line = get_model('order', 'Line')


class OrderLineApprovalListView(generic.ListView):

    template_name = 'oscar_approval/order_line_approval_list.html'
    search_form_class = forms.ApprovalSearchForm
    model = Line
    paginate_by = 10

    def get_queryset(self):
        qs = (self.model.objects.filter(
                    status=settings.OSCAR_LINE_APPROVAL_STATUS)
                  .select_related('product'))

        self.form = self.search_form_class(self.request.GET)
        if not self.form.is_valid():
            return qs

        q = self.form.cleaned_data['query']
        qs = qs.filter(product__title__icontains=q)

        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super(OrderLineApprovalListView, self).get_context_data(*args, 
                                                                      **kwargs)
        form = self.form if hasattr(self, 'form') else self.search_form()
        ctx['form'] = form
        return ctx


class OrderLineApproveView(generic.UpdateView):

    model = Line

    def post(self, request, *args, **kwargs):
        signals.order_line_approved.send(sender=self,
                                         line=self.get_object(),
                                         user=request.user)
        messages.success(request, _('Line purchase has been approved.'))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('approval:order-line-approval-list')


class OrderLineRejectView(generic.UpdateView):

    model = Line

    def post(self, request, *args, **kwargs):
        signals.order_line_rejected.send(sender=self,
                                         line=self.get_object(),
                                         user=request.user)
        messages.success(request, _('Line purchase has been rejected.'))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('approval:order-line-approval-list')
