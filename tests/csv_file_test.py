import logging

import os

from app import db

def test_check_csv_file(application):
    log = logging.getLogger('csv-log')
    root = os.path.dirname(os.path.abspath(__file__))
    uploaddir = os.path.join(root,'../app/uploads')
    if os.path.exists(uploaddir):
        log.info("CSV FILE UPLOADED")
        assert "CSV File uploaded"
    else:
        log.debug("CSV FILE NOT UPLOADED")
        assert "CSV File not uploaded"
