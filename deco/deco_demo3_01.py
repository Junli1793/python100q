import unittest
import functools


def skipIfNotDynamo(test_method):

    @functools.wraps(test_method)
    def wrapper(self):
        if not self.is_dynamo:
            raise unittest.SkipTest("Skip because it is not dynamo")

        return test_method(self)

    return wrapper


class DBTest(unittest.TestCase):

    def setUp(self):
        self.is_dynamo = True

    @skipIfNotDynamo        
    def test_account_ts(self):
        # Test code
        ...

