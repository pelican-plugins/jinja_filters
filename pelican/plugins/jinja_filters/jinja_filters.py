"""Various filters for Jinja."""

import logging

from titlecase import titlecase as _titlecase

from pelican.utils import SafeDatetime

__all__ = [
    "article_date",
    "breaking_spaces",
    "datetime",
    "titlecase",
]


LOG_PREFIX = "[Jinja Filters]"
logger = logging.getLogger(__name__)


def datetime(value, format_str="%Y/%m/%d %H:%M"):
    """
    Convert a datetime to a different format.

    The default format looks like --> 2016/11/25 12:34

    Args
    ----
        value (datetime.datetime): input date and time
        format_str (str): The datetime format string to apply to value

    Returns
    -------
        str: value, after the format_str has been applied

    """
    try:
        return value.strftime(format_str)
    except ValueError as e:
        logger.error(
            "%s ValueError. value: %s, type(value): %s, format_str: %s",
            LOG_PREFIX,
            value,
            type(value),
            format_str,
        )
        raise e


def article_date(value):
    """
    Convert a date to the format we want it displayed on the article template.

    Format looks like --> Friday, November 4, 2020

    Args
    ----
        value (datetime.datetime): input date

    Returns
    -------
        str: value, formatted nicely for displaying the date.

    """
    try:
        return "{dt:%A}, {dt:%B} {dt.day}, {dt.year}".format(dt=value)
    except ValueError as e:
        logger.error(
            "%s ValueError. value: %s, type(value): %s", LOG_PREFIX, value, type(value)
        )
        raise e


def datetime_from_period(value):
    """
    Converts "period" into a datetime object.

    On yearly/monthly/daily archive pages, a "period" object is supplied so you
    know what timeperiod the particular archive page is for. This converts it
    to a datetime.datetime object, so it can be further processed.

    If a month is not provided (i.e. the period is for a yearly archive),
    January is assumed. If a day is not provided (i.e. the period is for a
    yearly or monthly archive), the 1st is assumed.

    You can also generate a tuple of (up to three) integers to get a datetime
    out, using the integer representation for the month (1=January, etc).

    If passes a single integer, it is assumed to represent a year.

    Args
    ----
        value (tuple or int): input period

    Returns
    -------
        datetime.datetime: value converted

    """
    if isinstance(value, int):
        value = (value,)

    if len(value) >= 2 and isinstance(value[1], int):
        placeholder_month = SafeDatetime(2021, value[1], 1).strftime("%B")
    elif len(value) == 1:
        placeholder_month = SafeDatetime(2021, 1, 1).strftime("%B")
    else:
        placeholder_month = value[1]

    new_value = " ".join(
        (
            str(value[0]),
            placeholder_month,
            str(value[2]) if len(value) >= 3 else "1",
        )
    )
    new_datetime = SafeDatetime.strptime(new_value, "%Y %B %d")
    return new_datetime


def merge_date_url(value, url):
    """
    Given a Pelican setting URL that contains a placeholder for a date, and a
    date, it will combine the two to return the resulting URL.

    Args
    ----
        value (datetime.datetime): a date
        url (string): a Pelican URL setting

    Returns
    -------
        string: combined URL

    """
    try:
        return url.format(date=value)
    except ValueError:
        # will throw a "ValueError" if the value is a datetime.datetime and the url
        # contains a "-" (e.g. "{date:%-d}") (used in Pelican to strip the leading
        # zero)
        try:
            return url.format(date=SafeDatetime(value.year, value.month, value.day))
        except ValueError as e:
            logger.error(
                "%s ValueError. value: %s, type(value): %s, url: %s",
                LOG_PREFIX,
                value,
                type(value),
                url,
            )
            raise e


def breaking_spaces(value):
    """
    Convert non-breaking spaces to regular spaces.

    Args
    ----
        value (str): input value

    Returns
    -------
        str: the input string, now with regular spaces

    """
    return value.replace("\u00A0", " ")


def titlecase(value):
    """
    Returns the titlecased version of the supplied text.

    Args
    ----
        value (str): input value

    Returns
    -------
        str: value, titlecase formatted

    """
    return _titlecase(value)
