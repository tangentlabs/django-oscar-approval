from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from oscar.core.application import Application
from oscar.views.decorators import staff_member_required

from . import views

class ApprovalDashboardApplication(Application):
    name = None
    approvers_view = views.ApproverManagementView
    approver_update_view = views.ApproverUpdateView
    event_log_view = views.EventLogView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^approver-management/$', self.approvers_view.as_view(),
                name='approver-management'),
            url(r'^approver-management/add-approver/(?P<pk>\d+)/$',
                self.approver_update_view.as_view(),
                name='approver-add',
                kwargs={'is_approver': True}),
            url(r'^approver-management/remove-approver/(?P<pk>\d+)/$',
                self.approver_update_view.as_view(),
                name='approver-remove',
                kwargs={'is_approver': False}),
            url(r'^event-log/$',
                self.event_log_view.as_view(),
                name='approval-event-log'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required

application = ApprovalDashboardApplication()
