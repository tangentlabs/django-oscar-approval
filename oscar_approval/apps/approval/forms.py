from django import forms
from django.utils.translation import ugettext_lazy as _


class ApprovalSearchForm(forms.Form):

    query = forms.CharField(label=_('Search term'), required=False,
                            help_text=_('Search by product name'))
