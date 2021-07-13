from datetime import datetime
import unittest

from pelican.plugins.jinja_filters import jinja_filters
from pelican.utils import SafeDatetime


class Test_Merge_Date_URL(unittest.TestCase):
    YEAR_ARCHIVE_URL = "posts/{date:%Y}/"
    MONTH_ARCHIVE_URL = "posts/{date:%Y}/{date:%m}/"
    DAY_ARCHIVE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/"

    def test_year(self):
        my_date = datetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.YEAR_ARCHIVE_URL)
            == "posts/2016/"
        )

    def test_month(self):
        my_date = datetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.MONTH_ARCHIVE_URL)
            == "posts/2016/11/"
        )

    def test_day(self):
        my_date = datetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.DAY_ARCHIVE_URL)
            == "posts/2016/11/04/"
        )

    def test_pelican_year(self):
        my_date = SafeDatetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.YEAR_ARCHIVE_URL)
            == "posts/2016/"
        )

    def test_pelican_month(self):
        my_date = SafeDatetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.MONTH_ARCHIVE_URL)
            == "posts/2016/11/"
        )

    def test_pelican_day(self):
        my_date = SafeDatetime(2016, 11, 4, 12, 34)
        assert (
            jinja_filters.merge_date_url(my_date, self.DAY_ARCHIVE_URL)
            == "posts/2016/11/04/"
        )

    def test_pelican_strftime(self):
        my_date = datetime(2021, 7, 7, 0, 0)
        assert (
            jinja_filters.merge_date_url(
                my_date, "posts/{date:%Y}/{date:%-m}/{date:%-d}/"
            )
            == "posts/2021/7/7/"
        )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
