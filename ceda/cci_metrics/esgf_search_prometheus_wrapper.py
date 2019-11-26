from ceda.unittest_prometheus_wrapper.flask_app import flask_app_factory
from ceda.cci_odp_ops_tests.test_csw import CSWTestCase
from ceda.cci_odp_ops_tests.test_esgf_search import EsgfSearchTestCase
from ceda.cci_odp_ops_tests.test_ftp import FtpTestCase
from ceda.cci_odp_ops_tests.test_tds_opendap import TdsOpendapTestCase

''' Wrapper script to launch Flask app, to display results of esgf search unit tests
'''

app = flask_app_factory(EsgfSearchTestCase, test_names=['test01_search_all',
                        'test02_search_soilmoisture','test03_search_oceancolour',
                        'test04_cors'], service_name='esgf_search_test_cases')
