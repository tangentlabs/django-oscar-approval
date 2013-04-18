from functools import wraps

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import importlib

from . import access


def get_access_predicate():
    """
    Return the predicate function that indicates if a user can access the order
    approval views.
    """
    fn = getattr(settings, 'APPROVAL_ACCESS_CONTROL_FUNCTION', None)
    if fn is None:
        return access.is_order_approver
    if isinstance(fn, basestring):
        mod_path, fn_name = fn.rsplit('.', 1)
        mod = importlib.import_module(mod_path)
        return getattr(mod, fn_name)
    return fn


def order_approver_required(view_func):

    @wraps(view_func)
    def _check_approver(request, *args, **kwargs):
        if get_access_predicate()(request.user):
            return view_func(request, *args, **kwargs)
        messages.warning(
            request, _("You don't have permission to access this page"))
        return HttpResponseRedirect(reverse('customer:summary'))

    return _check_approver
