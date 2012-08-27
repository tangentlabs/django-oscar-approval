from django.conf.urls.defaults import patterns, url

from oscar.core.application import Application
from oscar.apps.dashboard.nav import register, Node

from . import views

node = Node('Approval', 'approver-management')
register(node, 100)


class ApprovalDashboardApplication(Application):
    name = None
    approvers_view = views.ApproverManagementView
    approver_update_view = views.ApproverUpdateView

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
        )
        return self.post_process_urls(urlpatterns)


application = ApprovalDashboardApplication()
