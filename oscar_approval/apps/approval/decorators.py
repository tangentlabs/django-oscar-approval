from functools import wraps

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


def order_approver_required(view_func):
    @wraps(view_func)
    def _check_approver(request, *args, **kwargs):
        if request.user.is_active and request.user.get_profile().is_order_approver:
            return view_func(request, *args, **kwargs)

        messages.warning(request, _("You don't have permission to access this page"))
        return HttpResponseRedirect(reverse('customer:summary'))

    return _check_approver
