from django.conf.urls.defaults import patterns, url

from oscar.core.application import Application

from . import views, decorators


class ApprovalApplication(Application):
    name = 'approval'
    approval_list_view = views.OrderLineApprovalListView
    approve_view = views.OrderLineApproveView
    reject_view = views.OrderLineRejectView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^order-line/list/$',
                self.approval_list_view.as_view(),
                name='order-line-approval-list'),
            url(r'^order-line/(?P<pk>\d+)/approve/$',
                self.approve_view.as_view(),
                name='order-line-approve'),
            url(r'^order-line/(?P<pk>\d+)/reject/$',
                self.reject_view.as_view(),
                name='order-line-reject'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return decorators.order_approver_required


application = ApprovalApplication()
