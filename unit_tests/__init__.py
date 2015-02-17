import logging
import os

from unittest import TestCase

SERVICE = "http://localhost:8092/wps"
TESTDATA = {}
CREDENTIALS = os.environ.get('TEST_CREDENTIALS')


from os.path import join, dirname
__testdata_filename__ = join(dirname(__file__), 'testdata.json')

try:
    from os.path import join
    import json
    with open(__testdata_filename__, 'r') as fp:
        TESTDATA = json.load(fp)
        # TODO: owslib does not like unicode
        for key in TESTDATA.keys():
            TESTDATA[key] = str(TESTDATA[key]) 
except:
    logging.error('could not read testdata! %s', __testdata_filename__ )


class WpsTestCase(TestCase):
    """
    Base TestCase class, sets up a wps
    """

    @classmethod
    def setUpClass(cls):
        from owslib.wps import WebProcessingService
        cls.wps = WebProcessingService(SERVICE, verbose=False, skip_caps=False)
