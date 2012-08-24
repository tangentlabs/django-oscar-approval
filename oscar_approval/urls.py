from django.conf.urls.defaults import patterns, url

from apps.approval import views

urlpatterns = patterns('',
    url(r'^order-line/list/$', views.OrderLineApprovalListView.as_view(),
        name='order-line-approval-list'),
    url(r'^order-line/(?P<pk>\d+)/approve/$', views.OrderLineApproveView.as_view(),
        name='order-line-approve'),
    url(r'^order-line/(?P<pk>\d+)/reject/$', views.OrderLineRejectView.as_view(),
        name='order-line-reject'),
)
