import logging
import os


def test_balance(application):
    log = logging.getLogger('balance-log')
    root = os.path.dirname(os.path.abspath(__file__))
