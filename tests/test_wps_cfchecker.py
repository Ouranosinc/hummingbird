import pytest

from tests.common import WpsTestClient, TESTDATA, assert_response_success

@pytest.mark.online
def test_wps_cfcheck():
    wps = WpsTestClient()
    datainputs = "[dataset={0}]".format(TESTDATA['noaa_nc_1'])
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='cfchecker',
                   datainputs=datainputs)
    assert_response_success(resp)

