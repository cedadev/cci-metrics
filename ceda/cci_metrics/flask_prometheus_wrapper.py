from ceda.unittest_prometheus_wrapper.flask_app import flask_app_factory
from ceda.unittest_prometheus_wrapper.test_data_container import TestDataContainer
from ceda.cci_odp_ops_tests.test_csw import CSWTestCase
from ceda.cci_odp_ops_tests.test_esgf_search import EsgfSearchTestCase
from ceda.cci_odp_ops_tests.test_ftp import FtpTestCase
from ceda.cci_odp_ops_tests.test_tds_opendap import TdsOpendapTestCase

import configparser
import os

import logging
logger = logging.getLogger('waitress')

''' Wrapper script to launch Flask app, to display results of various CCI services with unit tests
'''


def get_test_names(TestCase, test_sub_title='', restrict=None):
    ''' Detects unit test functions for TestCase objects. Functions must begin with 'test'
        Returns a list of test names to be passed into a TestDataContainer object

        `restrict` attribute is used to add only first X (e.g. 50) tests
    '''
    test_name_list = []

    for a, b in zip (TestCase.__dict__, range(len(TestCase.__dict__))):
        if restrict is not None:
            # Break before list appending because b starts at 0, existing test names begin at 1
            if b >= restrict:
                break

        if a.startswith('test'):
            test_name_list.append(a)

    return test_name_list


cci_data_containers = []

# Create the 4 containers to be tested for CCI
csw_container = TestDataContainer(CSWTestCase,
                                    test_names=get_test_names(CSWTestCase),
                                    service_name='csw_test_cases')
cci_data_containers.append(csw_container)

esgf_search_container = TestDataContainer(EsgfSearchTestCase,
                                            test_names=get_test_names(EsgfSearchTestCase),
                                            service_name='esgf_search_test_cases')
cci_data_containers.append(esgf_search_container)

ftp_container = TestDataContainer(FtpTestCase, test_names=get_test_names(FtpTestCase),
                                    service_name='ftp_test_cases')
cci_data_containers.append(ftp_container)

opendap_container = TestDataContainer(TdsOpendapTestCase, test_names=get_test_names(TdsOpendapTestCase),
                                        service_name='opendap_test_cases')
cci_data_containers.append(opendap_container)

'''
TDS OGC Services
'''

from ceda.tds_ogc_scan.test.test_wms import tds_wms_testcase_factory
from ceda.tds_ogc_scan.test.test_wcs import tds_wcs_testcase_factory


# TODO Change to environment variable or better solution?
CATALOG_URI = 'http://cci-odp-data.ceda.ac.uk/thredds/esacci/catalog.xml'


TdsWmsTestCase = tds_wms_testcase_factory(CATALOG_URI)
# Editing name attribute to dfferentiate it from Wcs test cases
# This means they'll have separate paths - /metrics/TdsCatalogServiceTestCaseWms
TdsWmsTestCase.__name__ = TdsWmsTestCase.__name__ + 'Wms'

tds_wms_container = TestDataContainer(TdsWmsTestCase, test_names=get_test_names(TdsWmsTestCase, restrict=5),
                                      service_name='tds_wms_test_cases')
cci_data_containers.append(tds_wms_container)


TdsWcsTestCase = tds_wcs_testcase_factory(CATALOG_URI)
TdsWcsTestCase.__name__ = TdsWcsTestCase.__name__ + 'Wcs'
tds_wcs_container = TestDataContainer(TdsWcsTestCase, test_names=get_test_names(TdsWcsTestCase, restrict=5),
                                      service_name='tds_wcs_test_cases')
cci_data_containers.append(tds_wcs_container)


app = flask_app_factory(cci_data_containers)
