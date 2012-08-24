from django.conf.urls.defaults import patterns, url

from apps.approval import views

urlpatterns = patterns('',
    url(r'^list/order-line/', views.OrderLineApprovalList.as_view(), 
        name='order-line-approval-list'),
)
