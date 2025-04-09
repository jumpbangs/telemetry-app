from datetime import datetime

from django.utils import timezone

from .constants import DateFormats


def get_formatted_date_only(date_str):
    print(f"date string passed is: {date_str}")
    if date_str is None:
        return None
    try:
        date = timezone.datetime.strptime(date_str, DateFormats.DATE_FORMAT_YYYY_MM_DD_T_HMS)
    except Exception:
        date = timezone.datetime.strptime(date_str, DateFormats.DATE_FORMAT_YYYY_MM_DD_T_HMSZ)

    final_date = date.strftime(DateFormats.DATE_FORMAT_YYYY_MM_DD)
    print(f"final date after conversion: {final_date}")
    return final_date


def get_current_formatted_date():
    current_date = datetime.now()
    date = current_date.strftime(DateFormats.DATE_FORMAT_YYYY_MM_DD)
    return date


def get_current_year():
    return datetime.today().year
