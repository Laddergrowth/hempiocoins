from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def hccoins_required(f):
    """
    Restrict access from users who have no hccoins.

    :return: Function
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.hccoins == 0:
            flash("Sorry, you're out of hccoins. You should buy more.",
                  'warning')
            return redirect(url_for('billing.purchase_hccoins'))

        return f(*args, **kwargs)

    return decorated_function
