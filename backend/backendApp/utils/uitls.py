def is_true_value(value):
    if value in ("True", "true", "1", True):
        return True
    else:
        return False


def is_none_or_empty(value):
    if value is None or value == "":
        return True
    else:
        return False


def is_paid_user_or_admin(user_role):
    return user_role == "P" or user_role == "A"


def is_user_admin(user_role):
    return user_role == "A"


def is_paid_user(user_role):
    return user_role == "P"
