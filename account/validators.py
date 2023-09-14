from django.core.exceptions import ValidationError
from django.core import validators as valid_m_in_dj
from django.utils.translation import gettext_lazy as _


def validate_email(value):
    email = valid_m_in_dj.EmailValidator(
        message=_("Please enter a valid email address."),
        code="invalid_email",
    )
    try:
        email(value)
        return value
    except ValidationError as e:
        raise ValidationError(e.messages, code=e.code)


def validate_password(value):
    regex = valid_m_in_dj.RegexValidator(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$',
        message=_("Password must contain at least one number and one uppercase and lowercase letter, and at least 8 or "
                  "more characters."),
        code="invalid_password",
    )
    try:
        regex(value)
        return value
    except ValidationError as e:
        raise ValidationError(e.messages, code=e.code)


def validate_code(value):
    code = valid_m_in_dj.RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message=_("Code must contain only letters and numbers."),
        code="invalid_code",
    )
    try:
        code(value)
        return value
    except ValidationError as e:
        raise ValidationError(e.messages, code=e.code)


