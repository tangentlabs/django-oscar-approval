from django import dispatch

order_line_approved = dispatch.Signal(providing_args=["line", "user"])
order_line_rejected = dispatch.Signal(providing_args=["line", "user"])
