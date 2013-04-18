def is_order_approver(user):
    """
    Default predicate for whether a user can approve orders
    """
    return user.is_active and user.get_profile().is_order_approver
