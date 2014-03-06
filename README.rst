django-oscar-approval
=====================

Order/Product approval extension for Django Oscar


Getting started
===============

Installation
------------

Add ``'oscar_approval'`` to ``INSTALLED_APPS`` and run::

    ./manage.py syncdb


Configuration
--------------

Edit your ``settings.py`` to set the following settings (example)::

    OSCAR_LINE_APPROVAL_STATUS = statuses.PENDING_AUTHORISATION
    OSCAR_ORDER_APPROVAL_STATUS = statuses.PENDING_AUTHORISATION

Include approval urls in your application::

    from oscar_approval.apps.approval.app import application as approval_application

    (r'^approval/', include(approval_application.urls)),


Integration into the project
-----------------------------
You may choose to integrate any of the following components:

1. Product model extension::

    from oscar_approval.apps.catalogue.abstract_models import AbstractProduct as ApprovalAbstractProduct

        ...
    class Product(AbstractProduct, ApprovalAbstractProduct):
        ...


2. Basic behaviour on receiving ``'order_placed'`` signal::

    from oscar.apps.order.signals import order_placed
    from oscar_approval.apps.order.receivers import receive_order_placed

    order_placed.connect(receive_order_placed)

This receiver simply sets ``OSCAR_LINE_APPROVAL_STATUS`` and ``OSCAR_ORDER_APPROVAL_STATUS`` for lines and orders that require approval.

3. Pin authorisation tab in the user profile:

    ...

4. Dashboard application for managing reviewers and viewing approval event logs:

    Extend user profile::

        from oscar_approval.apps.customer.abstract_models import AbstractProfile as ApproverProfile

        class Profile(ApproverProfile):
            ...

    Include dashboard application urls::

        from oscar_approval.apps.dashboard.app import application as approval_dashboard_application

        (r'^dashboard/approval/', include(approval_dashboard_application.urls))
