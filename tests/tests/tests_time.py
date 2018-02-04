import datetime
import pytz
import unittest

from django_generic.time import (SECOND, MINUTE, HOUR, DAY, WEEK, local_time_to_utc, string_to_datetime)


class TestTimeConstants(unittest.TestCase):
    def test_time_constants(self):
        self.assertEqual(SECOND, 1)
        self.assertEqual(MINUTE, 60)
        self.assertEqual(HOUR, 3600)
        self.assertEqual(DAY, 86400)
        self.assertEqual(WEEK, 604800)


class TestLocalTimeToUTC(unittest.TestCase):
    def test_local_time_to_utc(self):
        local_time = datetime.datetime(2017, 7, 20, 16)
        expected_time = datetime.datetime(2017, 7, 20, 14, tzinfo=pytz.utc)
        self.assertEqual(local_time_to_utc(local_time, 'Europe/Berlin'), expected_time)


class TestStringToDatetime(unittest.TestCase):
    def test_string_to_datetime(self):
        str_date = '2018-03-29T19:21:19.421Z'
        pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
        expected_date = datetime.datetime(year=2018, month=3, day=29, hour=19, minute=21, second=19)
        date = string_to_datetime(str_date, pattern)
        self.assertEqual(date, expected_date)
