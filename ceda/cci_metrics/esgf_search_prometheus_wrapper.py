from ceda.unittest_prometheus_wrapper.flask_app import flask_app_factory
from ceda.cci_odp_ops_tests.test_csw import CSWTestCase
from ceda.cci_odp_ops_tests.test_esgf_search import EsgfSearchTestCase
from ceda.cci_odp_ops_tests.test_ftp import FtpTestCase
from ceda.cci_odp_ops_tests.test_tds_opendap import TdsOpendapTestCase

''' Wrapper script to launch Flask app, to display results of esgf search unit tests
'''

if __name__ == '__main__':
    app_csw = flask_app_factory(CSWTestCase, test_names=['test01_csw_dashboard_query',
                                                        'test02_csw_dashboard_check_temporal_extent',
                                                        'test03_csw_dashboard_check_geographic_extent',
                                                        'test04_csw_l4_daily_faceted_search_query'],
                                service_name='csw_test_cases')

    app_esgf_search = flask_app_factory(EsgfSearchTestCase, test_names=['test01_search_all',
                                                                        'test02_search_soilmoisture',
                                                                        'test03_search_oceancolour',
                                                                        'test04_cors'], 
                                        service_name='esgf_search_test_cases')

    app_ftp = flask_app_factory(FtpTestCase, test_names=['test_01_change_to_top_dir', 
                                                        'test_02_list_cci_dir', 
                                                        'test_03_get_sea_level_readme'],
                                service_name='ftp_test_cases')

    app_opendap = flask_app_factory(TdsOpendapTestCase, test_names=['test01_dap', 'test02_dap', 
                                                                    'test03_dap'],
                                    service_name='opendap_test_cases')
