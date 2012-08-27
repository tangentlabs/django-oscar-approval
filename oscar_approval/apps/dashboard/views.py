from django.views import generic
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import Q, get_model
from django.contrib.auth.models import User

from oscar.apps.dashboard.users import forms


class ApproverManagementView(generic.ListView):

    template_name = 'oscar_approval/dashboard/approver_management.html'
    model = get_model(*settings.AUTH_PROFILE_MODULE.rsplit('.', 1))
    form_class = forms.UserSearchForm

    def get_queryset(self):
        qs = self.model.objects.none()

        if self.form.is_bound:
            cd = self.form.cleaned_data
            if not cd['email'] and not cd['name']:
                return self.model.objects.none()

            qs = (self.model.objects.all()
                        .select_related(settings.PROFILE_USER_RELATED_NAME))

            if cd['email']:
                qs = qs.filter(user__email__startswith=cd['email'])

            if cd['name']:
                parts = cd['name'].split()
                if len(parts) == 2:
                    qs = qs.filter(Q(user__first_name__istartswith=parts[0]) |
                                   Q(user__last_name__istartswith=parts[1])).distinct()
                else:
                    qs = qs.filter(Q(user__first_name__istartswith=cd['name']) |
                                   Q(user__last_name__istartswith=cd['name'])).distinct()
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super(ApproverManagementView, self).get_context_data(*args, 
                                                                   **kwargs)
        ctx['form'] = getattr(self, 'form', None) or self.form_class()
        ctx['profile_user_related_name'] = settings.PROFILE_USER_RELATED_NAME
        ctx['approvers'] = (self.model.objects.filter(is_order_approver=True)
                                    .select_related(settings.PROFILE_USER_RELATED_NAME))
        return ctx

    def get(self, request, *args, **kwargs):
        self.form = self.form_class(request.GET or None)

        if not self.form.is_valid() and self.form.is_bound:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)

        return super(ApproverManagementView, self).get(request, *args, **kwargs)


class ApproverUpdateView(generic.UpdateView):

    model = get_model(*settings.AUTH_PROFILE_MODULE.rsplit('.', 1))

    def post(self, request, *args, **kwargs):
        is_approver = bool(kwargs['is_approver'])

        profile = self.get_object()
        profile.is_order_approver = is_approver
        profile.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('approver-management')
