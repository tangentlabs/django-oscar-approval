from dango.db import models


class OrderLineApproval(models.Model):

    line = models.ForeignKey('order.Line')
    current_approval_level = models.IntegerField(null=True, blank=True)
